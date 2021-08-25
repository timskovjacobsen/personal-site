---
title: "Graham Scan algorithm for convex hulls"
date: 2021-08-10T10:56:59+02:00
tags: ["convex-hull", "algorithms", "computational-geometry"]
author: "Tim Skov Jacobsen"
description: "This is the description"
---

Have you ever wanted to compute the outer boundary of a bunch of scattered points? Maybe you have data in point cloud form from an object scan and want to detect the outer perimeter.

In this post, we will take a look at an efficient way of computing the so-called *convex hull* of a set of points in 2D.

{{% admonition tip "Convex Hull" %}}
A convex hull is a convex polygon that encloses all the points in a point set.

The convexity requirement dictates that if we were to follow the path around the convex hull in a counter-clockwise fashion, we must only make left turns.
{{% /admonition %}}

One way to efficiently compute the convex hull of an array of points is by using the *Graham Scan* algorithm. It has a time complexity of $O(n \log n)$, similar to many other algorithms for finding the convex hull.

## Visualizing the algorithm

Understanding the algorithm is easiest through an example. Let's consider the points in this plot

<center>

![points](/img/convex-hull/example/points.png)
</center>

### Preprocessing part

Before we start looping over the points to find the convex hull, we will do some setup or *preprocessing* or the problem:

1. The first thing to do is finding the source point, where we will start the algorithm from. Here, we will denote it as the **anchor point**.

    The anchor point is found as the point with the lowest $y$-coordinate. In case we have a tie, we take the point with the lowest $x$-coordinate among the ties.

    Visually, it's quite easy to see that **Point $12$** is the anchor point for this example.

2. Next, we need to sort our points according to their angle with the anchor point. E.g., for Point $13$, we would measure the angle between the $x$-axis and the line going through Point $12$ and $13$. The result of this sorting will dictate in which order we will process the points when finding the convex hull. While it's not strictly necessary, we can now remove the anchor point from the list.

    <center>

    ![angle sorting](/img/convex-hull/angle-sorting.svg)
    </center>

    where

    $$
    \alpha = \text{atan2}\left(\frac{\Delta y}{\Delta x}\right) = \text{atan2}\left(\frac{y_{15} - y_{12}}{x_{15} - x_{12}}\right)
    $$

3. Initialize a **stack** to store the convex hull points.

    At this state, we know that the anchor point is part of the convex hull, so we can already push that onto the stack. We are also guaranteed that the first point of the sorted list is part of the convex hull, so we push that to the stack as well. Take a couple of seconds to convince yourself that this point, i.e. Point $13$ in this example, will always be in the convex hull.

We then continue to the part where we loop through the points in the sorted order. The tasks 1. and 2. are explained in each iteration.

### Loop part

After preprocessing, we start the loop that eventually finds that convex hull.

In each loop, we perform two tasks:

1. A backtrack to see if any previously added points are still valid in the convex hull

    The backtracking can be explained like this:

    > If getting to the new point is **not a left turn**, the point in the current hull that was added latest should be removed. This point cannot possibly be in the convex hull as it violates the convex property.
    >
    > If a point is removed, look at the next point until we backtrack to a point that is valid.

2. Add the new point to the convex hull

Note that even though we always add the current point, it might be taken away again by the backtracking in task 1. in later iterations.

Let's go trough the reach iteration of the example to understand the loop part better.

#### Iteration 0

The loop starts by considering Point $8$, the next point in to our preprocessed, sorted list. It's easy to see that this will be the next point since it has the smallest angle with the anchor point and horizontal out of the points left to consider.

<center>

![iteration0](/img/convex-hull/example/iteration-0.png)
</center>

1. **Backtrack**  
  When travelling along the line $12 \rightarrow 13$ , getting to point $8$ is a left turn. Thus, we have have performed one backtracking step and found a valid point, so we remove nothing and continue.

2. **Add**  
  We add the new point $8$ to the convex hull.  
  
{{% admonition info %}}
*We can see by simple visual inspection that Point $8$ will be in the convex hull. But the algorithm does not know that yet.*
{{% /admonition %}}

#### Iteration 1

The next point in the sorted list is $14$.

<center>

![iteration1](/img/convex-hull/example/iteration-1.png)
</center>

1. **Backtrack**  
  When travelling along the line $13 \rightarrow 18$ , getting to point $14$ is a left turn. Thus, we have have performed one backtracking step and found a valid point, so we remove nothing and continue.

2. **Add**  
  We add point $14$ to the convex hull.
  
{{% admonition info %}}
Adding point $14$ might look weird here, as we can see that it should actually not be part of the convex hull. It will however be removed again later.
{{% /admonition %}}

#### Iteration 2

The next point is $15$.

<center>

![iteration2](/img/convex-hull/example/iteration-2.png)
</center>

1. **Backtrack**  
  When travelling along the line $8 \rightarrow 14$ , getting to point $15$ is a left turn. Thus, we have have performed one backtracking step and found a valid point, so we remove nothing and continue.

2. **Add**  
  We add point $15$ to the convex hull.

#### Iteration 3

On to point $6$. This iteration is where we will see the smart part of the Graham Scan algorithm, so pay close attention!

<center>

![iteration3](/img/convex-hull/example/iteration-3.png)
</center>

1. **Backtrack**  

    1. When travelling along the line $14 \rightarrow 15$ , getting to point $6$ is a *right* turn. In fact, a very sharp right turn.

        When we hit a right turn, we must remove the point in the convex hull that was added latest. Thus, we remove $15$ and continue backtracking.
  
    2. When travelling along the line $8 \rightarrow 14$ , getting to point $6$ is a *right* turn again.

        This means that we must remove $14$ and continue backtracking.

    3. When travelling along the line $13 \rightarrow 8$ , getting to point $6$ is a *left* turn again. We remove nothing and end the backtracking step.

2. **Add**  
  We add point $6$ to the convex hull.

Now we have a good grasp of the backtracking step, so we can write some pseudocode in Python-like syntax.

```python
for point in "sorted-points-except-anchor-and-second":
    while "getting-to-next-point-is-not-a-left-turn":
        convex_hull_stack.pop()
    convex_hull_stack.push(point)
```

Notice that the convex hull is modeled as a Stack abstract data type. As a **Last-In-First-Out** data structure, it works perfectly for the backtracking characteristic. We must always remove (or pop) the point in the current hull that was latest put in and must always add (or push) the new point onto the convex hull.

#### Iteration 4

We have now definitively ruled out points $14$ and $15$ as candidates for the convex hull, so we mark them as greyed out in the plot.

The next point to consider is $7$, as it has the smallest angle between the anchor point $12$ and horizontal out of the remaining points to consider.

<center>

![iteration4](/img/convex-hull/example/iteration-4.png)
</center>

1. **Backtrack**  

    1. When travelling along the line $8 \rightarrow 6$ , getting to point $7$ is a *right* turn. So we remove $6$ from the convex hull and continue backtracking.

    2. When travelling along the line $13 \rightarrow 8$ , getting to point $7$ is a *left* turn. So we remove remove nothing and exit backtracking.

2. **Add**  
  We add point $7$ to the convex hull and grey out $6$.

{{% admonition note %}}
Note that once we during a backtrack determine that a point is valid, that point is "locked" into the convex hull. We are sure that it should be in the final hull. We might backtrack to it again to realize it's valid once more though. In fact, this is the second time we backtracked to $8$.
{{% /admonition %}}

#### Iteration 5

The next point is $5$.

<center>

![iteration5](/img/convex-hull/example/iteration-5.png)
</center>

1. **Backtrack**  
    Seen from the line $8 \rightarrow 7$, reaching point $5$ is a left turn. We exit backtracking.

2. **Add**  
    We add point $5$ to the convex hull.

#### Iteration 6

The next point in our sorted list is $3$.

<center>

![iteration6](/img/convex-hull/example/iteration-6.png)
</center>

1. **Backtrack**  
    Getting to $3$ is a left turn, so we don't need to backtrack.

2. **Add**  
    We add point $3$ to the convex hull.

#### Iteration 7

The next point is $4$. Notice how point  $5$, $3$, and $4$ are (almost) colinear. They might not be exactly due to numerical inaccuracies, but let's assume for this explanation that they are colinear.

<center>

![iteration7](/img/convex-hull/example/iteration-7.png)
</center>

1. **Backtrack**

    1. When travelling along the line $5 \rightarrow 3$, getting to point $4$ is *not a left turn*. Since we assume the points are colinear, there is no turn at all. We remove point $3$ because it's the point in the hull that was latest added and continue backtracking.

    2. When travelling along the line $7 \rightarrow 5$, getting to point $4$ is *left turn*. We exit backtracking.

2. **Add**  
    We add point $4$ to the convex hull.

#### Iteration 8

The next point is $9$.

<center>

![iteration8](/img/convex-hull/example/iteration-8.png)
</center>

1. **Backtrack**  
    When travelling along the line $5 \rightarrow 4$, getting to point $9$ is a slight turn to the left. We don't backtrack on left turns.

2. **Add**  
    We add point $9$ to the convex hull.

#### Iteration 9

Point $1$ up next.

<center>

![iteration9](/img/convex-hull/example/iteration-9.png)
</center>

1. **Backtrack**
    1. From line $4 \rightarrow 9$, moving to point $1$ is a right turn. We know that point $9$ cannot be in the hull and remove it. Backtracking continues.

    2. Moving on to line $5 \rightarrow 4$, from which getting to point $1$ is also a right turn. We discard point $4$ as well and continue backtracking.

    3. Line $7 \rightarrow 5$ is now in consideration. Getting to point $1$ finally becomes a left turn and we can exit the backtracking without further removals.

2. **Add**  
    Point $1$ is added to the convex_hull.

#### Iteration 10

On to point $2$.

<center>

![iteration10](/img/convex-hull/example/iteration-10.png)
</center>

1. **Backtrack**
    1. Considering line $5 \rightarrow 1$, travelling to point $2$ requires a right turn. Point $1$ is removed and we can continue backtracking.
    2. We go back to line $7 \rightarrow 5$ and see a left turn to get to $2$, and exit backtracking.

2. **Add**  
    Add point $2$.

#### Iteration 11

On to point $11$.

<center>

![iteration11](/img/convex-hull/example/iteration-11.png)
</center>

1. **Backtrack**  
    Getting to point $11$ from $5 \rightarrow 2$ is a left turn. Done!

2. **Add**  
    Add point $11$

#### Iteration 12

Point $10$ is up next.

<center>

![iteration12](/img/convex-hull/example/iteration-12.png)
</center>

1. **Backtrack**

    1. Getting to point $10$ from $2 \rightarrow 11$ is a right turn. Remove $11$ and continue to backtrack.

    2. Getting to point $10$ from $5 \rightarrow 2$ is a left turn. No need to backtrack anymore.

2. **Add**  
    Add point $10$.

#### Final convex hull

There are no more points left to consider. We finish the convex hull by connecting the last point to the anchor point and we are done!

<center>

![final-hull](/img/convex-hull/example/final-hull.png)
</center>

## Comments

### Time complexity

You might be wondering why the time complexity of the algorithm becomes $O(n \log n)$.

{{% admonition note "Sorting governs time complexity" %}}
The sorting in Step 2 of the preprocessing part is the critical element for the time complexity of the algorithm, since it is the computationally most expensive thing we are doing. The fastest sorting algorithms run in $O(n \log n )$, which makes Graham Scan an $O(n \log n)$ algorithm.
{{% /admonition %}}

In the loop, we are only backtracking a few steps in each iteration. This can be regarded as constant time, i.e. $O(1)$. Therefore we can say that the loop has $O(n)$ time complexity. Had the backtracking step gone all the way back to the anchor point each time, we would have a time complexity of $O(n²)$. Fortunately, the algorithm is smarter than that.

This brings us to

$$
O(n \log n) + O(n) \Longrightarrow O(n \log n)
$$

### Detecting direction of turns

As we've seen, the algorithm relies heavily on determining which way we must turn to get to the next point. If we consider the triangle formed by the two last points added to the current convex hull and the new point, we can compute the determinant to find its area.

If we arrange the points correctly according to our chosen counter-clockwise order, the sign of the area will reveal whether getting to the new point is a left or right turn. Or even if the points are colinear.

Let's say we have $k$ points in a current convex hull called $h$. We then consider the line from $h[k-1] \rightarrow h[k]$. We can then say the following about the turn required to get to a new point $p$.

<center>

| Area sign | Direction for turn |
| :--- | :--- |
| Positive | Getting to point $p$ requires a left turn, i.e. a counter-clockwise turn |
| Negative | Getting to point $p$ requires a right turn, i.e. a clockwise turn |
| Zero | The points $h[k-1]$, $h[k]$ and $p$ are on a straight line, i.e. colinear |
</center>

With all the information above, we can begin writing an implementation.

## Implementation

Before we get to implementing the actual Graham Scan algorithm, let's create some point objects that we can work with.

```python
# core.py
from __future__ import annotations
from math import atan2
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def angle(self, other: Point):
        """Return the angle between a line a horizontal.

        The line is defined by the instance and another point."""
        dx = self.x - other.x
        dy = self.y - other.y
        return atan2(dy, dx)

    def distance_to(self, other: Point):
        """Return the Euclidian distance to from the point to another point."""
        dx = self.x - other.x
        dy = self.x - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def determinant(self, other1, other2):
        """Return the determinant of the three points.

        The determinant represents the area of the triangle formed by the points.

        We consider the line from `other1` to `other2`. The turn to get to point
        `self` can be described by the determinant.

        If the determinant is:
            Positive: getting to `self` is a left (counter-clockwise) turn
            Negative: getting to `self` is a right (clock-wise turn) turn
            zero: All three points are on a straight line (colinear)
        """
        x1, y1 = other1.x, other1.y
        x2, y2 = other2.x, other2.y

        # Compute determinant
        return (x2 - x1) * (self.y - y1) - (y2 - y1) * (self.x - x1)

```

With the simple `Point` class above, we can write the Graham Scan algorithm.

We use two helper methods `pop_anchor_point` and `is_not_left_turn` to make the `convex_hull_graham_scan` function more tidy and make it read almost like pseudocode.

```python
# convex_hull.py
from typing import List, Tuple
from math import atan2

from core import Point


def pop_anchor_point(points: List[Point]) -> Point:
    """Return the anchor point from a list of 2D points and remove it from
    the list.

    Parameters
    ----------
    points
        The list of points from which to extract the anchor point

    Returns
    -------
    The anchor point, i.e. the point with the smallest y-coordinate.
    If multiple points have the smallest y-coordinate, the point with
    the smallest x-coordinate among those is returned.

    Note
    ----
    This function mutates the input list.
    """
    anchor = points[0]
    anchor_index = 0

    # Loop over the array of points, excluding the first point
    for i, p in enumerate(points[1:], start=1):

        is_y_smaller = p.y < anchor.y
        is_y_equal_and_x_smaller = p.y == anchor.y and p.x < anchor.x

        if is_y_smaller or is_y_equal_and_x_smaller:
            # New anchor point found
            anchor = p
            anchor_index = i

    # Return the anchor point and remove it from the array
    return points.pop(anchor_index)


def is_not_left_turn(new_point: Point, point_from: Point, point_to: Point) -> bool:
    """Return True if getting to `new_point` is not a left turn.

    We travel along the line `point_from` --> `point_to`"""
    area = new_point.determinant(point_from, point_to)
    return True if area <= 0 else False


def convex_hull_graham_scan(points: List[Point]) -> List[Point]:
    """Return the convex hull using the Graham Scan algorithm."""

    # Create a copy of the input list to avoid mutating it
    xy_points = points[:]

    # Extract the anchor as the point with min y-coordinate, lowest x in case of a tie
    anchor = pop_anchor_point(xy_points)

    # Sort points acc. to their angle measured from the x-axis to the anchor point in
    # counter-clockwise direction. In case of ties, sort by distance from anchor point.
    xy_points.sort(key=lambda p: (p.angle(anchor), (p.distance_to(anchor))))

    # Initialize the list of hull points with the anchor and the first point in the
    # sorted points list. These are both guaranteed to be in the convex hull
    # This hull list works as a stack, where we add and pop points as needed. Thus,
    # a point that are added to the hull in an intermediate step might be removed if
    # as we gain more information during the algorithm's execution.
    hull = [anchor, xy_points[0]]

    for point in xy_points[1:]:

        # Backtrack to see if any points in the current hull need to be removed
        while is_not_left_turn(point, hull[-2], hull[-1]):
            # CASE 1:
            # THe determinant was negative, i.e. the point is on the right side of
            # the line segment formed by the last two point in the hull. Thus, the
            # current last point in the hull list cannot possibly be in the hull.

            # CASE 2:
            # The determinant was 0, i.e. the three points are colinear.
            # We discard the middle point, i.e. the last point in the current hull
            hull.pop()

        # When we get here, the point must be on the left side of the line segment,
        # Thus, we add it to the convex hull.
        # Note that the point is not necessarily part of the final convex hull as it
        # might be removed in future backtracking steps.
        hull.append(point)

    return hull
```

## References

For a more detailed explanation of the Graham Scan algorithm, check out [*Introduction to Algorithms, 3rd Edition*](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844).
