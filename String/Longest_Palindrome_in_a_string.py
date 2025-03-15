class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0
        max_length = 1

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes
            length1 = expand_around_center(i, i)
            if length1 > max_length:
                max_length = length1
                start = i - (length1 - 1) // 2

            # Even length palindromes
            length2 = expand_around_center(i, i + 1)
            if length2 > max_length:
                max_length = length2
                start = i - (length2 - 2) // 2

        return s[start:start + max_length]


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
        "racecar",
        "aaaaabbbbaaaa"
    ]

    for test_case in test_cases:
        result = solution.longestPalindrome(test_case)
        print(f"Input: '{test_case}'")
        print(f"Longest palindrome: '{result}'")
        print()
