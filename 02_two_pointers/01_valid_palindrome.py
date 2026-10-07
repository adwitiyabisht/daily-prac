"""
NeetCode: Valid Palindrome (LC 125)
Category: Two Pointers
NeetCode Link: https://neetcode.io/problems/is-palindrome
Target Complexity: O(n) Time, O(1) Auxiliary Space
"""


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1

        while r > l and not alphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1

    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
     ord('a') <= ord(c) <= ord('z') or
     ord('0') <= ord(c) <= ord('9'))

if __name__ == "__main__":
    # Standard positive & negative cases
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False

    # Edge cases (empty or space-only string, single character)
    assert is_palindrome(" ") is True
    assert is_palindrome("") is True
    assert is_palindrome("a.") is True
    assert is_palindrome(".,") is True

    # Case insensitivity & alphanumeric check
    assert is_palindrome("0P") is False
    assert is_palindrome("Was it a car or a cat I saw?") is True

    print("✓ All tests passed!")