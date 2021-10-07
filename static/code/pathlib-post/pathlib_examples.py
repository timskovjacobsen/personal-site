from pathlib import Path


def generate_tree() -> None:
    desktop = Path().home() / "Desktop"

    files_in_foo = ["file1.txt", "file2.txt", "file3.txt", "mod1.py", "mod2.py"]
    files_in_baz = ["data1.csv", "data2.csv", "coolscript.sh"]

    (desktop / Path("foo")).mkdir(parents=True, exist_ok=True)
    for f in files_in_foo:
        (desktop / Path("foo") / Path(f)).touch(exist_ok=True)

    (desktop / Path("foo/bar")).mkdir(parents=True, exist_ok=True)
    for f in files_in_baz:
        (desktop / Path("foo/bar") / Path(f)).touch(exist_ok=True)


# Create the directory tree
generate_tree()

foo_dir = Path().home() / "Desktop/foo"
bar_dir = foo_dir / "bar"
file1 = foo_dir / "file1.txt"

# Get file name with extension
file1.name  # file1.txt
print(file1.name)

# Get file name without extension
file1.stem
print(file1.stem)

# Get file extension
file1.suffix
print(file1.suffix)

#

# Iterate over files in a directory
for f in foo_dir:
    print(f)

# Get all files of certain extension in a directory
foo_files = foo_dir.glob("*.py")
for f in foo_files:
    print(f)

# Prints:
# mod1.py
# mod2.py
