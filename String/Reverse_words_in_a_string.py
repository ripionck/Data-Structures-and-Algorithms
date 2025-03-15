class Solution:

    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()

        # Reverse the order of words
        words.reverse()

        # Join the words back into a string
        return ' '.join(words)


if __name__ == "__main__":

    # Example usage for reverseWords
    solution = Solution()

    # Test case 1
    s1 = "the sky is blue"
    print(f"Original: '{s1}'")
    print(f"Reversed: '{solution.reverseWords(s1)}'")

    # Test case 2
    s2 = "  hello world  "
    print(f"Original: '{s2}'")
    print(f"Reversed: '{solution.reverseWords(s2)}'")

    # Test case 3
    s3 = "a good   example"
    print(f"Original: '{s3}'")
    print(f"Reversed: '{solution.reverseWords(s3)}'")
