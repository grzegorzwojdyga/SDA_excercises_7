import variables
import unittest
from ddt import ddt, data


class Test_TestTask1(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(variables.task1(3, 4), 7)

    def test_float(self):
        self.assertEqual(variables.task1(5, 3), 8)


@ddt
class Test_TestTask2(unittest.TestCase):
    @data((2, 4), (5, 25))
    def test_integer(self, value):
        input, output = value
        self.assertEqual(variables.task2(input), output)

    def test_doc(self):
        self.assertTrue("Input" in variables.task2.__doc__)


class TestTask(unittest.TestCase):
    """
    Write some test for variables, text_operation or coleection module (rememmber to change name) 
    Try to crash it and improve a little bit, use parametrization with other arguments (like strings)
    """
    pass


if __name__ == '__main__':
    unittest.main()
