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
    def test_input_part_1_end_result(self):
        from aoc_2021.solutions.day3_A import get_gamma, get_epsilon_from_gamma
        test_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        
        gamma = get_gamma(test_input)
        epsilon = get_epsilon_from_gamma(gamma)
        result = gamma * epsilon
        assert result == 198

    def test_input_part_2_end_result(self):
        from aoc_2021.solutions.day3_B import get_list_matching_criteria, get_list_matching_criteria, get_int_from_bit
        test_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
        
        oxygen_rating = get_list_matching_criteria(test_input, True)
        co2_scrubber = get_list_matching_criteria(test_input, False)
        result = get_int_from_bit(oxygen_rating) * get_int_from_bit(co2_scrubber)
        assert result == 230