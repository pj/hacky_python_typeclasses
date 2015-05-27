#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.


class Either(object):
    def __init__(self, left=None, right=None):
        assert left is None or right is None
        assert left is not None or right is not None
        self._left = left
        self._right = right


def Left(_left):
    return Either(left=_left)


def Right(_right):
    return Either(right=_right)
