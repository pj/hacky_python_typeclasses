#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

from typeclass import typemethod


class Monad(object):
    pass


@typemethod(Monad)
def point(klass, value):
    raise NotImplementedError()


@typemethod(Monad)
def bind(m, func):
    raise NotImplementedError()
