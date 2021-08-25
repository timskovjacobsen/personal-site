---
title: "Why indexing starts at 0"
date: 2021-05-24T10:56:59+02:00
tags: ["arrays", "c", "programming", "pointers"]
categories: ["programming", "c"]
moreData: true
---

My first programming experience was in [Matlab](https://www.mathworks.com/products/matlab.html). A high-level language built for technical computing. In Matlab, indexing start at 1, which I at the time never thought twice about.

I have been teaching Python to engineers with non-software background internally at work for some time, and I often get the question

> Why does indexing start at $0$ instead of $1$?

People quickly get used to indexing starting at $0$ though. After all, it's a pretty easy adjustment to the coding habits. But why *do* arrays start at $0$ in some languages?  

For this explanation, we will take a brief look at the C programming language.
## The C language

C is one of the oldest programming languages still used today. It's a low-level language where you write code closer to the computer's hardware compared to higher-level languages like Java and Python.

Since C operates closer to hardware, many things are left to the programmer to deal with such as memory allocation, correctly passing arguments to functions etc. Most other languages are built on top of C, providing easier ways to deal with those somewhat tedious tasks and lowering the bar for entry into programming.

In C, the concept of **pointers** is extremely important. We don't need to understand much of it for this post, but in short

 > A pointer is a variable whose value is the memory address of another variable.

Pointers are used to manipulate variables and arrays at a lower level. To avoid having copies of variables flying around in our C code, we instead pass around information saying "you can find the value at this location".

Let's take a further look at this in relation to **arrays** where indexing comes into play.

## Index 0 is the array itself

Suppose we have an array of integers

```c
int arr[] = {123, 221, 173};
```

We just established above that a pointer's value is a memory address. So how to point to an array consisting of multiple integers, which each must have their own address in memory?

{{% admonition success "" %}}
Pointing to an array in C points to the first element in the array
{{% /admonition %}}

So the array pointer is pointing to the first element, but that does not really justify why index $0$ should be the first index.
This makes more sense when we try to *offset* to get elements further down the array.

We can think of it this way:

<center>

| Element   | Offset from first element |
| :--------: |:---------------:  |
| $1$     | $0$                 |
| $2$    | $1$                 |
| $i$  | $i-1$             |
</center>

Or as a formula

$$
\text{value at index} = *( \text{array pointer} + \text{index} )
$$

Where $\text{array pointer}$ is the first element of the array and the $\text{index}$ denotes the offset.

The $\*$ before the parenthesis denotes that we want the *value* stored at the memory location, not the memory location itself. The memory location would be a hex number.

When we view an index in this fashion, namely as an offset from the first element's memory location, it makes sense to use $0$-indexing.

{{% admonition question "What about indexing strings?" %}}
Strings are just arrays of characters under the hood, so it works in the same way.
{{% /admonition %}}

## In summary

The $0$-indexing in most languages stems from array pointers in C pointing to the first element in the array. The index is viewed as an offset from the first element. Thus, index $0$ is the first element.

Some scientific programming languages like Matlab and Fortran choose to use $1$-indexing instead to make it more intuitive for people who don't have computer science background.
