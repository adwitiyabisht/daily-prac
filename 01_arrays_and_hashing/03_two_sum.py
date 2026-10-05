"""
NeetCode: Two Sum (LC 1)
Category: Arrays & Hashing
NeetCode Link: https://neetcode.io/problems/two-integer-sum
Target Complexity: O(n) Time, O(n) Space
"""


def two_sum(nums: list[int], target: int) -> list[int]:

    map = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in map:
            return [map[difference], index]
        map[num] = index
    return

if __name__ == "__main__":
    # Standard cases
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]

    # Edge cases (negative values, zeros)
    assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4]
    assert sorted(two_sum([0, 4, 3, 0], 0)) == [0, 3]

    print("✓ All tests passed!")