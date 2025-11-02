import os

def clear_clutter(folder):
    os.chdir(folder)
    files = os.listdir(folder)
    extensions = set()

    for file in files:
        if os.path.isfile(file):
            name, ext = os.path.splitext(file)
            if ext:
                extensions.add(ext.lower())

    for ext in extensions:
        count = 1
        for file in os.listdir(folder):
            if file.endswith(ext):
                new_name = f"{count}{ext}"  # ✅ fixed here
                os.rename(file, new_name)
                print(f"Renamed: {file} --> {new_name}")
                count += 1

# ✅ use raw string for path
folder = r"D:\1986\PYTHON\BASIC_python\myenv"
clear_clutter(folder)
