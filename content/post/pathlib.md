---
title: "Useful snippets from Python's pathlib"
date: 2021-09-15T10:56:59+02:00
tags: ["pathlib", "python", "file-system", "directories", "files"]
author: "Tim Skov Jacobsen"
draft: true
description: "A collection of examples using Python's pathlib"
---

## Getting the file part of a path

```python
p.name
```

## Getting the file's extension

```python
p.suffix
```

## Get the file name without extension

```python
p.stem
```

## Changing extension of a file

p.with_suffix(".txt")

## Get all files of certain extension from directory

Returns a generator

```python
some_dir.glob("*.pdf")
```

## Implementation of pathlib (REPHRASE!)

The `/` operator for concatenating paths is implemented by the `__truediv__` magic method.


