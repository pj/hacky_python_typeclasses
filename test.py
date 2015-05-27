#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

import unittest

from typeclass import FunctionImportException
from functor import fmap
from option import Nothing, Some
from either import Either, Left, Right

import either_instances
import option_instances
import list_instances


def never_called():
    raise Exception("this should never be called")


class TestOption(unittest.TestCase):
    def test_functor(self):

        # basic test
        a = fmap(Nothing(), never_called)

        self.assertEqual(a._value, None)

        b = fmap(Some("foo"), lambda x: x + "bar")

        self.assertEqual(b._value, "foobar")

        c = fmap(Some("foo"), lambda x: x + "bar")

        d = fmap(c, lambda x: "baz")

        self.assertEqual(d._value, "baz")

        # Check that calling the underlying fmap raises an exception
        with self.assertRaises(FunctionImportException):
            option_instances.fmap(Nothing, never_called)


class TestList(unittest.TestCase):
    def test_functor(self):
        b = fmap([], never_called)

        self.assertEqual(b, [])

        a = fmap([1, 2, 3, 4], lambda x: x + 1)

        self.assertEqual(a, [2, 3, 4, 5])

        c = fmap([1, 2, 3, 4], lambda x: "asdf")

        self.assertEqual(c, ["asdf", "asdf", "asdf", "asdf"])

        with self.assertRaises(FunctionImportException):
            list_instances.fmap([], never_called)


class TestEither(unittest.TestCase):
    def test_basics(self):
        with self.assertRaises(AssertionError):
            Either(left=None, right=None)

        with self.assertRaises(AssertionError):
            Either(left="asdf", right="qwer")

    def test_functor(self):
        a = fmap(Left("Something bad happened"), never_called)

        self.assertEqual(a._right, None)
        self.assertEqual(a._left, "Something bad happened")

        b = fmap(Right("foo"), lambda x: x + "bar")

        self.assertEqual(b._right, "foobar")
        self.assertEqual(b._left, None)

        c = fmap(Right("foo"), lambda x: "baz")

        self.assertEqual(c._right, "baz")
        self.assertEqual(c._left, None)

        # Check that calling the underlying fmap raises an exception
        with self.assertRaises(FunctionImportException):
            either_instances.fmap(Left("x"), never_called)


if __name__ == '__main__':
    unittest.main()
