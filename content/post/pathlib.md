---
title: "Examples from Python's pathlib"
date: 2021-09-15T10:56:59+02:00
tags: ["pathlib", "python", "file-system", "directories", "files"]
author: "Tim Skov Jacobsen"
draft: true
description: "A collection of examples using Python's pathlib"
---

## Introduction

I often have to lookup the API for Python's pathlib library. This blog post aims to collect many of pathlib's methods into a single resource. It's supposed to be a lookup tool without too much explanation for each example. It therefore assumes some familiarity of pathlib and its benefits over the `os` module as well as general Python knowledge.

## Boilerplate for running the examples

For the examples, we'll import the `Path` class from pathlib and create a directory and a file.

```shell
$ tree
.
└── foo
    ├── bar
    │   ├── coolscript.sh
    │   ├── data1.csv
    │   └── data2.csv
    ├── file1.txt
    ├── file2.txt
    ├── file3.txt
    ├── mod1.py
    └── mod2.py

2 directories, 8 files
```

```python
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
```

All examples below assume that this code has been run.

## Get current working directory

```python
Path().cwd()
```

## Get file name with extension

```python
file1.name       # file1.txt
```

## Get the file name without extension

```python
file1.stem       # file1
```

## Get the file extension

```python
file1.suffix    # .txt
```

## Change file name

```python
file1.with_name("new_file_name")      # new_file_name.txt
```

## Change file extension

```python
file1.with_suffix(".json")      # file1.json
```

## Get all files of certain extension in a directory

Pathlib includes all/most of the features of the glob module. So we can use glob patterns on a path to returns a generator.

```python
foo_files = foo_dir.glob("*.py")
for f in foo_files:
    print(f)

# Prints:
#   mod1.py
#   mod2.py
```

## Implementation of pathlib (REPHRASE!)

The `/` operator for concatenating paths is implemented by the `__truediv__` magic method.
