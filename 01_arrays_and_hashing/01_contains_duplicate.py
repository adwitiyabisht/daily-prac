"""
NeetCode: Contains Duplicate / Has Duplicate (LC 217)
Category: Arrays & Hashing
NeetCode Link: https://neetcode.io/problems/duplicate-integer
Time Complexity: O(n)
Space Complexity: O(n)
"""

def has_duplicate(nums: list[int]) -> bool:

    hashset = set()

    for n in nums:
        if n in hashset:
            return True

        hashset.add(n)

    return False
        

if __name__ == "__main__":
    # NeetCode Example 1
    assert has_duplicate([1, 2, 3, 3]) is True

    # NeetCode Example 2
    assert has_duplicate([1, 2, 3, 4]) is False

    # Edge cases (empty array, single element)
    assert has_duplicate([]) is False
    assert has_duplicate([1]) is False

    print("✓ NeetCode assertions passed!")