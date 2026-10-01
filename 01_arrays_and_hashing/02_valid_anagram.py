"""
NeetCode: Valid Anagram (LC 242)
Category: Arrays & Hashing
NeetCode Link: https://neetcode.io/problems/is-anagram
Target Complexity: O(n) Time, O(1) or O(k) Space (where k is alphabet size)
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

"""
Alternative 1 line solutions:

return sorted(s) == sorted(t)

return Counter(s) == Counter(t)
"""


if __name__ == "__main__":
    # Standard positive & negative cases
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False

    # Edge cases (unequal lengths, identical single characters, distinct single characters)
    assert is_anagram("a", "ab") is False
    assert is_anagram("a", "a") is True
    assert is_anagram("ab", "a") is False

    # Character frequency count edge cases
    assert is_anagram("aa", "a") is False
    assert is_anagram("aacc", "ccac") is False

    print("✓ All tests passed!") 