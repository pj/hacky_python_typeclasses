#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""

"""

class Option(object):
    def __init__(self, value):
        self._value = value

#class Nothing(Option):
#    def __init__(self):
#        Option.__init__(self, None)
#
#
#class Some(Option):
#    def __init__(self, value):
#        Option.__init__(self, value)
#

def Nothing():
    return Option(None)

def Some(value):
    return Option(value)

def isEmpty(opt):
    if opt._value is None:
        return True
    else:
        return False
