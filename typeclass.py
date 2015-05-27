#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

type_dispatch_table = {}


class typemethod(object):
    def __init__(self, klass):
        self._klass = klass

    def __call__(self, func):
        class dispatcher(object):
            def __init__(self, underlying_func):
                self._underlying_func = underlying_func

            def __call__(self, *args, **kwargs):
                first_arg = args[0]

                if type(first_arg) is type:
                    first_arg_klass = first_arg
                    args = args[1:]
                else:
                    first_arg_klass = type(args[0])

                typefunc = type_dispatch_table.get((first_arg_klass, func))
                print first_arg_klass, func
                print type_dispatch_table

                if typefunc is None:
                    return func(*args, **kwargs)
                else:
                    return typefunc(*args, **kwargs)

        return dispatcher(func)


class FunctionImportException(Exception):
    pass


class typeinstance(object):
    def __init__(self, instance_klass, dispatch):
        self._instance_klass = instance_klass
        self._dispatcher = dispatch

    def __call__(self, func):
        # register function with dispatch
        key = (self._instance_klass, self._dispatcher._underlying_func)
        type_dispatch_table[key] = func

        # Don't allow this function to be imported
        def bad_import(*args, **kwargs):
            raise FunctionImportException()

        return bad_import
