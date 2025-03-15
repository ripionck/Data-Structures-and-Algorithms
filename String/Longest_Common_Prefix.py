from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string in the list
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]

        return shortest


# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test cases for Longest Common Prefix
    prefix_test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        ["throne", "throne"],
        ["", "b"],
        ["a"],
        []
    ]

    print("Longest Common Prefix:")
    for case in prefix_test_cases:
        result = solution.longestCommonPrefix(case)
        print(f"Input: {case}")
        print(f"Longest common prefix: '{result}'")
        print()
