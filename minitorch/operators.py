"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(x: float, y: float) -> float:
    """$f(x, y) = x * y$"""
    return x * y
# TODO fill in the remaining mathematical operators. Use mul provided above as an example.
# - id
def id(x: float) -> float:
    return x
# - add
def add(x: float, y: float) -> float:
    return x + y
# - neg
def neg(x: float) -> float:
    return -x
# - lt
def lt(x: float, y: float) -> float:
    return 1.0 if x < y else 0.0
# - eq
def eq(x: float, y: float) -> float:
    return 1.0 if x == y else 0.0
# - max
def max(x: float, y: float) -> float:
    return x if x > y else y
# - is_close
def is_close(x: float, y: float) -> float:
    return 1.0 if abs(x - y) < 1e-2 else 0.0
# - sigmoid
def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))
# - relu
def relu(x: float) -> float:
    return x if x > 0 else 0
# - log
def log(x: float) -> float:
    return math.log(x)
# - exp
def exp(x: float) -> float:
    return math.exp(x)
# - log_back
def log_back(x: float, d: float) -> float:
    return d / x
# - inv
def inv(x: float) -> float:
    return 1.0 / x
# - inv_back
def inv_back(x: float, d: float) -> float:
    return -d / (x * x)
# - relu_back
def relu_back(x: float, d: float) -> float:
    return d if x > 0 else 0

# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
def map(xs: list[float], fn: Callable[[float], float]) -> list[float]:
    return [fn(x) for x in xs]
# - zipWith
def zipWith(xs: list[float], ys: list[float], fn: Callable[[float, float], float]) -> list[float]:
    return [fn(x, y) for x, y in zip(xs, ys)]
# - reduce
def reduce(fn: Callable[[float, float], float], xs: list[float]) -> float:
    if not xs:
        return 0.0
    result = xs[0]
    for x in xs[1:]:
        result = fn(result, x)
    return result
#
# Use these to implement
# - negList : negate all elemnts in a list using map
def negList(xs: list[float]) -> list[float]:
    return map(xs, lambda x: neg(x))
# - addLists : add corresponding elements from two lists using zipWith
def addLists(xs: list[float], ys: list[float]) -> list[float]:
    return zipWith(xs, ys, add)
# - sum: sum all elements in a list using reduce
def sum(xs: list[float]) -> float:
    return reduce(add, xs)
# - prod: calculate the product of all elements in a list using reduce
def prod(xs: list[float]) -> float:
    return reduce(mul, xs)


# TODO: Implement for Task 0.3.
