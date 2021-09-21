---
title: "Python list comprehensions"
date: 2021-05-25T10:56:59+02:00
tags: ["python", "list-comprehension", "examples"]
draft: true
author: "Tim Skov Jacobsen"
description: "This is the description"
---

## List comprehensions

List comprehensions is a Python ... TODO

{{% admonition tip "Run the code" %}}
All code snippets in this post should be directly runnable in a Python interpreter when copied. Run the code and make small variations to get a better feel for how it behaves.
{{% /admonition %}}

## The most simple form

When `isinstance(st)` is `True`.

{{< highlight python "linenos=false" >}}
x = [1, 2, 4, 5, -1, 1, 5, -3]
# Subtract one from each element

x1 = [elem - 1 for elem in x]
{{< / highlight >}}

```python
x = [1, 2, 4, 5, -1, 1, 5, -3]
# Subtract one from each element

x1 = [elem - 1 for elem in x]
```


{{< highlight python "linenos=true" >}}
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
result_list = expression1 if condition else expression2 for item in iterable
{{< / highlight >}}

Note that in the first list comprehension for X_non_str, the order is:

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

## References

* [PEP 202 - List Comprehensions](https://www.python.org/dev/peps/pep-0202/) The Python Enhancement Proposal (PEP) that lead to list comprehensions being part of the language.
