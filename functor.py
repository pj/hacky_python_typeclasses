#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""

"""
from typeclass import typemethod

class Functor(object):
    pass

@typemethod(Functor)
def fmap(box, func):
    raise NotImplementedError()
