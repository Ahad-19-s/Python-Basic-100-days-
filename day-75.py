#!/usr/bin/env python3
"""
pdf_tool.py — Multipurpose PDF utility using pypdf

Features:
 - merge: Merge multiple PDFs into one
 - split: Split a PDF into single-page PDFs (or a page range)
 - rotate: Rotate pages (all or range)
 - watermark: Stamp each page with a watermark PDF (first page of watermark file)
 - encrypt: Add password protection to a PDF
 - decrypt: Try to open and save an encrypted PDF (requires password)
 - extract-text: Extract text from a PDF to a .txt file

Usage examples:
  python pdf_tool.py merge -o output.pdf a.pdf b.pdf c.pdf
  python pdf_tool.py split input.pdf --pages-per-file 1 -d outdir
  python pdf_tool.py rotate input.pdf -o rotated.pdf --angle 90
  python pdf_tool.py watermark -i target.pdf -w stamp.pdf -o stamped.pdf
  python pdf_tool.py encrypt -i in.pdf -o out_encrypted.pdf --password hunter2
  python pdf_tool.py decrypt -i secret.pdf -o decrypted.pdf --password hunter2
  python pdf_tool.py extract-text -i input.pdf -o output.txt
"""
import argparse
import os
import sys
from typing import List, Optional

from pypdf import PdfReader, PdfWriter, PdfMerger
from pypdf.errors import PdfReadError


def merge_pdfs(inputs: List[str], output: str) -> None:
    merger = PdfMerger()
    for pdf in inputs:
        if not os.path.isfile(pdf):
            raise FileNotFoundError(f"Source file not found: {pdf}")
        merger.append(pdf)
    with open(output, "wb") as f:
        merger.write(f)
    merger.close()
    print(f"Merged {len(inputs)} files → {output}")


def split_pdf(input_pdf: str, out_dir: str, pages_per_file: int = 1, range_pages: Optional[str] = None) -> None:
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    reader = PdfReader(input_pdf)
    pages = list(reader.pages)

    # If user provided a page-range like "3-7", convert to 0-based indices
    if range_pages:
        start, end = map(int, range_pages.split("-", 1))
        pages = pages[start - 1:end]  # inclusive

    total = len(pages)
    file_index = 0
    for i in range(0, total, pages_per_file):
        writer = PdfWriter()
        chunk = pages[i:i + pages_per_file]
        for p in chunk:
            writer.add_page(p)
        out_path = os.path.join(out_dir, f"{os.path.splitext(os.path.basename(input_pdf))[0]}_part{file_index + 1}.pdf")
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"Wrote {len(chunk)} pages → {out_path}")
        file_index += 1


def rotate_pdf(input_pdf: str, output: str, angle: int, pages_range: Optional[str] = None, clockwise: bool = True) -> None:
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for idx, page in enumerate(reader.pages):
        apply_rotation = True
        if pages_range:
            # pages_range expected like "2-5" or "3"
            if "-" in pages_range:
                s, e = pages_range.split("-", 1)
                s, e = int(s), int(e)
                apply_rotation = (s - 1) <= idx <= (e - 1)
            else:
                p = int(pages_range)
                apply_rotation = (idx == p - 1)
        if apply_rotation:
            if clockwise:
                page.rotate_clockwise(angle)
            else:
                page.rotate_counter_clockwise(angle)
        writer.add_page(page)

    with open(output, "wb") as f:
        writer.write(f)
    print(f"Saved rotated PDF → {output}")


def watermark_pdf(input_pdf: str, watermark_pdf: str, output: str, first_page_only: bool = False) -> None:
    # watermark_pdf should be a PDF where we use the first page as stamp
    wm_reader = PdfReader(watermark_pdf)
    wm_page = wm_reader.pages[0]
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for idx, page in enumerate(reader.pages):
        # merge_page overlays the watermark on the page (in-place)
        # Note: merge_page alters the page object; maintain copy semantics by using the page directly
        page.merge_page(wm_page)
        writer.add_page(page)
        if first_page_only:
            # if only first page should be watermarked, add subsequent pages unchanged
            for j in range(idx + 1, len(reader.pages)):
                writer.add_page(reader.pages[j])
            break

    with open(output, "wb") as f:
        writer.write(f)
    print(f"Watermarked PDF → {output}")


def encrypt_pdf(input_pdf: str, output: str, password: str, owner_password: Optional[str] = None, use_128bit: bool = True) -> None:
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for p in reader.pages:
        writer.add_page(p)
    # encrypt: user password is the one required to open; owner password controls permissions
    writer.encrypt(user_pwd=password, owner_pwd=owner_password, use_128bit=use_128bit)
    with open(output, "wb") as f:
        writer.write(f)
    print(f"Encrypted {input_pdf} → {output}")


def decrypt_pdf(input_pdf: str, output: str, password: Optional[str] = None) -> None:
    try:
        reader = PdfReader(input_pdf)
    except PdfReadError as e:
        # try opening with password
        if password is None:
            raise e
        reader = PdfReader(input_pdf, password=password)

    # if PDF is still encrypted, try to decrypt
    if reader.is_encrypted and password is not None:
        reader.decrypt(password)

    writer = PdfWriter()
    for p in reader.pages:
        writer.add_page(p)
    with open(output, "wb") as f:
        writer.write(f)
    print(f"Decrypted (or re-saved) → {output}")


def extract_text(input_pdf: str, output_txt: str) -> None:
    reader = PdfReader(input_pdf)
    with open(output_txt, "w", encoding="utf-8") as out:
        for i, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""
            out.write(f"\n\n--- Page {i} ---\n\n")
            out.write(text)
    print(f"Extracted text → {output_txt}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="pdf_tool — manipulation utilities using pypdf")
    sub = p.add_subparsers(dest="command", required=True)

    # merge
    m = sub.add_parser("merge", help="Merge multiple PDFs into one")
    m.add_argument("inputs", nargs="+", help="Input PDF files in order")
    m.add_argument("-o", "--output", required=True, help="Output merged PDF path")

    # split
    s = sub.add_parser("split", help="Split a PDF into multiple PDFs")
    s.add_argument("input", help="Input PDF")
    s.add_argument("-d", "--out-dir", required=True, help="Output directory")
    s.add_argument("--pages-per-file", type=int, default=1, help="Number of pages per output file (default:1)")
    s.add_argument("--range", help="Optional page range to split, e.g. 3-8")

    # rotate
    r = sub.add_parser("rotate", help="Rotate pages")
    r.add_argument("input", help="Input PDF")
    r.add_argument("-o", "--output", required=True, help="Output PDF")
    r.add_argument("--angle", type=int, choices=[90, 180, 270], default=90, help="Rotation angle clockwise")
    r.add_argument("--pages", help="Page or range to rotate, e.g. 2 or 3-7 (default: all)")
    r.add_argument("--counter", action="store_true", help="Rotate counter-clockwise instead")

    # watermark
    w = sub.add_parser("watermark", help="Apply watermark (overlay) using first page of watermark PDF")
    w.add_argument("-i", "--input", required=True, help="Input PDF")
    w.add_argument("-w", "--watermark", required=True, help="Watermark PDF (use its first page)")
    w.add_argument("-o", "--output", required=True, help="Output PDF")
    w.add_argument("--first-only", action="store_true", help="Apply watermark to first page only")

    # encrypt
    e = sub.add_parser("encrypt", help="Encrypt PDF with a password")
    e.add_argument("-i", "--input", required=True, help="Input PDF")
    e.add_argument("-o", "--output", required=True, help="Output PDF")
    e.add_argument("--password", required=True, help="Password to open the PDF")
    e.add_argument("--owner-password", help="Owner password (optional)")
    e.add_argument("--use-128", action="store_true", help="Use 128-bit encryption (default True)")

    # decrypt
    d = sub.add_parser("decrypt", help="Decrypt (open and re-save) PDF")
    d.add_argument("-i", "--input", required=True, help="Input (encrypted) PDF")
    d.add_argument("-o", "--output", required=True, help="Output (decrypted) PDF")
    d.add_argument("--password", help="Password to open the PDF if required")

    # extract text
    x = sub.add_parser("extract-text", help="Extract text from a PDF")
    x.add_argument("-i", "--input", required=True, help="Input PDF")
    x.add_argument("-o", "--output", required=True, help="Text file to write extracted text to")

    return p


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "merge":
            merge_pdfs(args.inputs, args.output)
        elif args.command == "split":
            split_pdf(args.input, args.out_dir, pages_per_file=args.pages_per_file, range_pages=args.range)
        elif args.command == "rotate":
            rotate_pdf(args.input, args.output, args.angle, pages_range=args.pages, clockwise=not args.counter)
        elif args.command == "watermark":
            watermark_pdf(args.input, args.watermark, args.output, first_page_only=args.first_only)
        elif args.command == "encrypt":
            encrypt_pdf(args.input, args.output, args.password, owner_password=args.owner_password,
                        use_128bit=args.use_128)
        elif args.command == "decrypt":
            decrypt_pdf(args.input, args.output, password=args.password)
        elif args.command == "extract-text":
            extract_text(args.input, args.output)
        else:
            parser.print_help()
    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
