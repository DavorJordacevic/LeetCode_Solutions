# https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        # Define the Roman numeral symbols and their corresponding values
        roman_numerals = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        # Initialize an empty string to store the Roman numeral representation
        roman = ''
        # Iterate through the Roman numeral symbols in descending order
        for value, symbol in sorted(roman_numerals.items(), reverse=True):
            # Repeat the symbol as many times as possible while its value is less than or equal to the number
            while num >= value:
                roman += symbol
                num -= value
        return roman
