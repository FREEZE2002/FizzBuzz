# test_fizzbuzz.py
import unittest
from fizzbuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzBuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzBuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")

    def test_other_numbers(self):
        self.assertEqual(fizzBuzz(7), "7")

if __name__ == "__main__":
    unittest.main()
