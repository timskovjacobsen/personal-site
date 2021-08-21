---
title: "Python list comprehensions"
date: 2021-05-25T10:56:59+02:00
tags: ["python", "list-comprehension", "examples"]
draft: true
author: "Tim Skov Jacobsen"
description: "This is the description"
---

This is the initial post

```python
for post in posts:
    print(post)
```

When `isinstance(st)` is `True`.

```python
# Original list
X = [1.5, 2.3, 4.4, 5.4, 'n', 1.5, 5.1, 'a']

# Extract non-strings from X to new list
# - when using only 'if', put 'for' in the beginning
X_non_str = [el for el in X if not isinstance(el, str)]

# Change all strings in X to 'b', preserve everything else as is
# - when using 'if' and 'else', put 'for' in the end
X_str_changed = ['b' if isinstance(el, str) else el for el in X]
```

Note that in the first list comprehension for X_non_str, the order is:

## List comprehension with *if*

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

## List comprehension with *if/else*

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
