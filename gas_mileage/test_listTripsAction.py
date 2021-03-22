"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import gas_mileage


class TestListTripsAction(unittest.TestCase):
    def input_replacement(self, prompt):
        self.assertFalse(self.too_many_inputs)
        self.input_given_prompt = prompt
        r = self.input_response_list[self.input_response_index]
        self.input_response_index += 1
        if self.input_response_index >= len(self.input_response_list):
            self.input_response_index = 0
            self.too_many_inputs = True
        return r

    def print_replacement(self, *text, **kwargs):
        line = " ".join(text) + "\n"
        self.printed_lines.append(line)
        return

    def setUp(self):
        self.too_many_inputs = False
        self.input_given_prompt = None
        self.input_response_index = 0
        self.input_response_list = [""]
        gas_mileage.input = self.input_replacement

        self.printed_lines = []
        gas_mileage.print = self.print_replacement
        return

    def test001_listTripsActionExists(self):
        self.assertTrue('listTripsAction' in dir(gas_mileage),
                        'Function "listTripsAction" is not defined, check your spelling')
        return

    def test002_listTripsActionDoesNotUpdate(self):
        from gas_mileage import listTripsAction
        notebook = []
        expected = []

        self.input_response_list = ["???"]
        listTripsAction(notebook)
        self.assertListEqual(expected, notebook, "Your listTripsAction made changes to the notebook when it shouldn't")
        self.assertGreaterEqual(len(self.printed_lines), 1, 'Make sure to print a message to the user about no trips being recorded')

    def test003_listTripsActionPrintLines(self):
        from gas_mileage import listTripsAction
        notebook = [
            {'date': "01/01/17", 'miles': 100.0, 'gallons': 5.0},
            {'date': "01/02/17", 'miles': 300.0, 'gallons': 10.0}
        ]
        expected = [
            {'date': "01/01/17", 'miles': 100.0, 'gallons': 5.0},
            {'date': "01/02/17", 'miles': 300.0, 'gallons': 10.0}
        ]

        self.input_response_list = ["???"]
        listTripsAction(notebook)
        self.assertListEqual(expected, notebook, "Your listTripsAction made changes to the notebook when it shouldn't")
        self.assertGreaterEqual(len(self.printed_lines), 2, 'You should print a line for each trip')

        printed_text = "".join(self.printed_lines)

        self.assertIn("01/01/17", printed_text)
        self.assertIn("100.0", printed_text)
        self.assertIn("5.0", printed_text)
        self.assertIn("20.0", printed_text)
        self.assertIn("01/02/17", printed_text)
        self.assertIn("300.0", printed_text)
        self.assertIn("10.0", printed_text)
        self.assertIn("30.0", printed_text)


if __name__ == '__main__':
    unittest.main()
