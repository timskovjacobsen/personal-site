---
title: "Python list comprehensions"
date: 2021-05-25T10:56:59+02:00
tags: ["python", "list-comprehension", "examples"]
draft: true
author: "Tim Skov Jacobsen"
description: "This is the description"
---

## Prerequisites

Prerequisites for reading this article is basic Python knowledge. To get most out of it you should be able to

* Create a list
* Write conditional statements (`if`, `elif`, `else`)
* Create a `for` loop
* Define a function

## List comprehensions

List comprehensions is a Python ... TODO

{{% admonition tip "Run the code" %}}
All code snippets in this post should be directly runnable in a Python script when copied. As a result, each code block has some deliberate duplication.

Run the code and make small variations to get a better feel for how it behaves.
{{% /admonition %}}

## The most simple form

### Copy a list

The simplest form of a list comprehension is to just create a copy of a list. I.e. insert the elements into the new list one by one

```python
x = [1, 2, 4, 5, -1, 1, 5, -3]

# Copy the list element by each element
x0 = [elem for elem in x]

print(x0)  # [1, 2, 4, 5, -1, 1, 5, -3]
```

This is not very exciting or useful though, as copying a list is better done with `x.copy()` or `x[:]`.

### Traditional loop

If we compare the code above to the equivalent traditional `for` loop, we realize why list comprehensions are considered more readable by many.

```python
x = [1, 2, 4, 5, -1, 1, 5, -3]

x_new = []
# Copy the list element by element
for elem in x:
    x_new.append(elem)

print(x_new)  # [1, 2, 4, 5, -1, 1, 5, -3]
```

Even in the simplest case, we are essentially replacing the three lines needed for creating the empty list, the for loop and the append method with only a single line that reads like English.

As an added bonus, list comprehensions are also faster than traditional loops.

### Calculate on each element

As more useful example, we can perform an expression that contains each element.

The example below multiplies each element by `2`.

```python
x = [1, 2, 4, 5, -1, 1, 5, -3]

# Multiply each element by 2
x_new = [2 * elem for elem in x]

print(x_new)  # [2, 4, 8, 10, -2, 2, 10, -6]
```

Notice the order of first having the *expression*, which in this case is `2 * elem` and then the `for` loop

In the copy example from above, the expression was simply the element itself.

### Run a function on each element

The *expression* can be any valid Python code. Let's define a function that triples its input. We can use this function as part of an expression and pass each element as argument.

```python
def triple(number):
    return number * 3

    
x = [1, 2, 4, 5, -1, 1, 5, -3]

x_new = [triple(elem) for elem in x]

print(x_new)  # [3, 6, 12, 15, -3, 3, 15, -9]
```

So the expression was now `triple(elem)`, which returned the value and put it into the list.

## Variation with conditional if

General syntax

{{< highlight python "linenos=false" >}}
result_list = expression for item in iterable if condition
{{< / highlight >}}

An English-like version with descriptive variable names

{{< highlight python "linenos=false" >}}
ripe_apples = extract_apple for apple in apple_box if apple_is_ripe
{{< / highlight >}}

The readability of Python really shows here. A person without coding experience could on the surface understand what this line does.

* `ripe_apples`: ss...
* `extract_apple`: expression that filters

<!-- $$
\mathtt{ripe\\_apples} = [ \overbrace{\text{extract_apple}}^{\text{expression that filters} } \ \mathtt{for} \ \overbrace{\text{apple}}^{\text{each apple}} \ \mathtt{in} \ \ \ \text{apple_box} \ \ \ \mathtt{if} \ \ \ \text{apple_is_ripe} \ ]
$$ -->

## Variation with conditional if/else

and in the last list comprehension for X_str_changed, the order is:

{{< highlight python "linenos=false" >}}
result_list = expression1 if condition else expression2 for item in iterable
{{< / highlight >}}

I always find it hard to remember that expression1 has to be before if and expression2 has to be after else. My head wants both to be either before or after.

I guess it is designed like that because it resembles normal language, e.g. "I want to stay inside if it rains, else I want to go outside"

In plain English the two types of list comprehensions mentioned above could be stated as:

With only if:

> extract_apple for apple in apple_box if apple_is_ripe

and with if/else

> mark_apple if apple_is_ripe else leave_it_unmarked for apple in apple_box

```python
result = "Yes" if done >= 0 else "No"
```

## Examples (Should maybe be another article)

### Filtering a list

### Calling a function on list

## Unpacking

```python
[(p.x, p.y) for ]
```

## When not to use list comprehensions

List comprehensions should only be used when a list should be returned. The examples above all show such scenarios.

A standard example that is **not** suited for a list comprehension is using `print` as the expression

```python
[print(elem) for elem in x]  # Don't do this
```

**Instead**, use a traditional for loop which does not expect all iterations to end up as list elements

```python
# Do this instead
for elem in x:
    print(elem)
```

Another example is plotting. E.g. do not so something like this

```python
import matplotlib.pyplot as plt

# <some code prior to plotting>

[plt.plot(...) for ... in ...]  # Don't do this

```

Both these are examples of expressions that have side-effects rather than simply returning an element to be part of the resulting list.

## References

* [PEP 202 - List Comprehensions](https://www.python.org/dev/peps/pep-0202/) The Python Enhancement Proposal (PEP) that lead to list comprehensions being part of the language.
