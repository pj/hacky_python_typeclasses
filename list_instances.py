#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""

"""

import functor
from typeclass import typeinstance


@typeinstance(list, functor.fmap)
def fmap(_list, func):
    return map(func, _list)
