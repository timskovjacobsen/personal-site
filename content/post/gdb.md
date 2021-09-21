---
title: "Debugging C code with gdb"
date: 2021-08-29T10:56:59+02:00
tags: ["C", "programing", "debugging", "gdb", "algorithms"]
draft: true
author: "Tim Skov Jacobsen"
description: "How to use the GNU debugger to debug your C code"
---

## Compile

Before we can debug anything, we must compile the program. The compile command we normally use to run the program is of little help. It will make us lose a lot of relevant information we care about for debugging.

Instead, we use the `-g` flag to compile, which retains the useful debugging information in the compiled file. With a program called `foo` we could use

    gcc -Wall -g foo.c

This should give us a `a.out` file in the working directory, which is what the debugger will work with.

I've quoted some info from the manual pages for `gcc` regarding debugging and the `-g` flag. You can check this information yourself with `man gcc` in your terminal, although the output is rather long and tedious to read through.

{{% admonition quote "From man pages of gcc" %}}
*To tell GCC to emit extra information for use by a debugger, in almost all cases you need only to add `-g` to your other options.*
{{% /admonition %}}

{{% admonition quote "From man pages of gcc, re. -g flag" %}}
*`-g`: Produce debugging information in the operating system's native format (stabs, COFF, XCOFF, or DWARF). GDB can work with this debugging information.*

*On most systems that use stabs format, `-g` enables use of extra debugging information that only GDB can use; this extra information makes debugging
work better in GDB but probably makes other debuggers crash or refuse to
read the program.*
{{% /admonition %}}

## Start gdb

We now have a compiled executable `a.out` ready to be debugged. We start the debugger with

    gdb a.out

If the program takes arguments, we can also supply them while invoking the debugger. Say we wanted to compute $c² = a² + b²$ with positional arguments $a=3$ and $b=4$, we would run

    gdb --args a.out 3 4

This will enter the debugger indicated by the `(gdb)` prompt.

## Set a breakpoint

To set a breakpoint at line 15

    (gdb) break 15

## Run the program

    (gdb) run
