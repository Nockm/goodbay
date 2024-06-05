import os
import unittest

from libs.examples.example_module import get_sum_of_numbers
from libs.system.file_data_io import load_local_json, save_local_json, get_local_dir

script_dir = os.path.dirname(os.path.realpath(__file__))


class TestExampleModule(unittest.TestCase):
    def test_add_two_numbers(self):
        input: list[str] = load_local_json(__file__, "input/input.json")
        output = get_sum_of_numbers(input) # type: ignore
        get_local_dir(__file__, "output_expected", make_empty=True)
        save_local_json(__file__, "output_expected/output.json", output)
