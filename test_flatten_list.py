import unittest

from flatten_list import flatten_list


class TestFlattenList(unittest.TestCase):
    def test_one_level_of_nesting(self):
        self.assertEqual(flatten_list([1, 2, [3], [4, 5]]), [1, 2, 3, 4, 5])

    # TODO: add a test for deeper nesting, e.g. [1, [2], [3, [4, 5, [6]]], 7]

    # TODO: add a test for an already-flat list, e.g. [1, 2, 3]

    # TODO: add a test for an empty list


if __name__ == "__main__":
    unittest.main()
