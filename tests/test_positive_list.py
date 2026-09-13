#!/usr/bin/env python3
"""Tests for the Positive List assignment."""

import unittest
from unittest.mock import patch

import numpy as np

from src.positive_list import positive_list


class TestPositiveList(unittest.TestCase):
    """positive_list(L) -> list of only the strictly positive values in L."""

    def test_worked_example(self):
        L = [2, -2, 0, 1, -7]
        result = positive_list(L)
        self.assertIsInstance(
            result,
            list,
            msg="positive_list should return a list. Got %s."
            % (type(result),),
        )
        self.assertEqual(
            result,
            [2, 1],
            msg="positive_list(%r) should be [2, 1]: 0 and negative values "
            "are excluded, and order is preserved." % (L,),
        )

    def test_random_values_keep_only_positives(self):
        for i in range(4):
            L = np.random.randint(-100, 100, 50)
            result = positive_list(L)
            self.assertIsInstance(
                result,
                list,
                msg="positive_list should return a list. Got %s."
                % (type(result),),
            )
            correct = [x for x in L if x > 0]
            self.assertEqual(
                result,
                correct,
                msg="Wrong result for list %r! Expected %r, got %r."
                % (L, correct, result),
            )

    def test_zero_is_excluded(self):
        result = positive_list([0, 0, 0])
        self.assertEqual(
            result,
            [],
            msg="positive_list([0, 0, 0]) should be []: zero is not "
            "positive, so it must not be included.",
        )

    def test_empty_list_gives_empty_list(self):
        result = positive_list([])
        self.assertEqual(
            result,
            [],
            msg="positive_list([]) should be [] for an empty input list.",
        )

    def test_uses_filter(self):
        with patch('builtins.filter') as f:
            positive_list([2, -2, 0, 1, -7])
            f.assert_called()


if __name__ == '__main__':
    unittest.main()
