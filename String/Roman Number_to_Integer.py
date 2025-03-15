class Solution:

    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev_value = 0
        for char in reversed(s):
            current_value = roman_values[char]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        return total

    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC",
                   "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = []
        for i, value in enumerate(values):
            while num >= value:
                num -= value
                roman.append(symbols[i])
        return ''.join(roman)


# Example usage
if __name__ == "__main__":

    solution = Solution()

    # Test cases for Roman to Integer
    roman_test_cases = ["III", "LVIII", "MCMXCIV"]
    print("Roman to Integer:")
    for roman in roman_test_cases:
        result = solution.romanToInt(roman)
        print(f"Roman: {roman}, Integer: {result}")
    print()

    # Test cases for Integer to Roman
    int_test_cases = [3, 58, 1994]
    print("Integer to Roman:")
    for num in int_test_cases:
        result = solution.intToRoman(num)
        print(f"Integer: {num}, Roman: {result}")
