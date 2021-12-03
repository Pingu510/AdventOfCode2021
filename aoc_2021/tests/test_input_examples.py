import pytest

class Test_Hello:
    def test_greeting(self):        
        from aoc_2021.solutions import helpers
        name = "Frida"

        result = helpers.hello(name)
        assert result == "Hello " + name

class Test_Day1:
    def test_part_A_example_input(self): 
        from aoc_2021.solutions import day1_A
        test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

        result = day1_A.get_increases(test_input)
        assert result == 7

    def test_part_B_example_input(self):  
        from aoc_2021.solutions.day1_B import get_average_increase    
        test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

        result = get_average_increase(test_input)
        assert result == 5

class Test_Day2:
    def test_part_A_example_input(self):
        from aoc_2021.solutions.day2_A import get_resulting_position
        test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

        result = get_resulting_position(test_input)
        assert result == 150

    def test_part_B_example_input(self):
        from aoc_2021.solutions.day2_B import get_resulting_position
        test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
        
        result = get_resulting_position(test_input)
        assert result == 900

class Test_Day3:
    def test_gamma_with_test_input(self):
        test_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        print(int(test_input[0], 1))