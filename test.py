import bmi_Calculator
import json


class TestClass:

    def test_function(self):
        fp = fp = open('inputdata.json',)
        inputdata = json.load(fp)
        output = bmi_Calculator.calculateBmi(inputdata)
        print(output)
        assert output["Msg"] == 'Success'


t1 = TestClass()
t1.test_function()
