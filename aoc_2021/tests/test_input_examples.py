import pytest
import code
from code.day1_1 import hello_me

class Test_Hello:
    def test_greeting(self):
        hi = hello_me()
        assert hi == "Hello"

class Test_DayOne:
    def test_example_input(self):  
        from code.day1_1 import get_increases    
        input_test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        result = get_increases(input_test)
        assert result == 7


class Test_DayTwo:
    def test_example_input(self):  
        from code.day1_2 import get_average_increase    
        input_test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        result = get_average_increase(input_test)
        assert result == 5
