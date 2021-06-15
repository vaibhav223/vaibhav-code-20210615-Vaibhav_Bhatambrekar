import bmi_Calculator
import json


class TestClass:

    def test_function_1(self):
        # Override the Python built-in input method
        fp = fp = open('inputdata.json',)
        inputdata = json.load(fp)
        # Call the function you would like to test (which uses input)
        output = bmi_Calculator.calculateBmi(inputdata)
        assert output == 'expected_output'
        return "Success"


t1 = TestClass()
print(t1.test_function_1())
