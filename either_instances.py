#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

import functor
import monad

from either import Either, Right
from typeclass import typeinstance


@typeinstance(Either, functor.fmap)
def fmap(either, func):
    if either._left is None:
        return Right(func(either._right))
    else:
        return either


@typeinstance(Either, monad.point)
def point(value):
    return Right(value)


@typeinstance(Either, monad.bind)
def bind(either, func):
    if either._left is None:
        return func(either._right)
    else:
        return either
