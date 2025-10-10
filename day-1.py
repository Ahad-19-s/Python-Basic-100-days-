# love_calc_percent.py
# Deterministic "love percentage" from two names.
# Same input -> same output (no randomness).

import hashlib

def love_percentage(name1: str, name2: str) -> int:
    """
    Deterministically compute a "love percentage" from two names.
    Uses SHA1 on the normalized concatenation of names,
    then maps to 0..100.
    """
    a = name1.strip().lower()
    b = name2.strip().lower()
    if not a or not b:
        raise ValueError("Both names must be non-empty.")

    combo = f"{a}:{b}"
    # SHA1 is deterministic; hex digest to integer
    h = hashlib.sha1(combo.encode("utf-8")).hexdigest()
    # take a slice and convert to int
    val = int(h[:8], 16)  # use first 8 hex digits
    percent = val % 101   # map to 0..100
    return percent

def main():
    print("=== Love Calculator (Percent) ===")
    n1 = input("Enter first name: ").strip()
    n2 = input("Enter second name: ").strip()
    try:
        pct = love_percentage(n1, n2)
    except ValueError as e:
        print("Error:", e)
        return
    print(f"\n{name_display(n1, n2, pct)}")

def name_display(n1, n2, pct):
    heart = "❤️" if pct >= 70 else "💛" if pct >= 40 else "💔"
    return f"{n1} + {n2} = {pct}% {heart}"

if __name__ == "__main__":
    main()
