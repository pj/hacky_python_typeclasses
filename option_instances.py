#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""

"""

from typeclass import typeinstance
import functor
from option import Option, isEmpty


@typeinstance(Option, functor.fmap)
def fmap(opt, func):
    if isEmpty(opt):
        return opt
    else:
        return Option(func(opt._value))
