import unittest
from merge import merge


class TestMerge(unittest.TestCase):
    ''' Tests for merge function. '''

    def test_successful_merge(self):
        ''' Successful merge with example input from coding task. '''

        # Arrange
        input = [[25, 30], [2, 19], [14, 23], [4, 8]]
        expected_output = [[2, 23], [25, 30]]

        # Act
        output = merge(input)

        # Assert
        self.assertEqual(expected_output, output)

    def test_empty_input_merge(self):
        ''' Empty list should return an empty list. '''

        # Arrange
        input = []
        expected_output = []

        # Act
        output = merge(input)

        # Assert
        self.assertEqual(expected_output, output)

    def test_wrong_input_merge(self):
        ''' Wrong input results in ValueError. '''

        # Arrange
        input = 'Wrong input'

        # Assert
        with self.assertRaises(ValueError):
            # Act
            merge(input)

    def test_wrong_input_in_list_merge(self):
        ''' Wrong input within the list results in ValueError. '''

        # Arrange
        input = ['Wrong input', 34]

        # Assert
        with self.assertRaises(ValueError):
            # Act
            merge(input)


if __name__ == '__main__':
    unittest.main()
