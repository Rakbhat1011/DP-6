"""
A palindrome mirrors around its center; there are 2n‑1 centers (between chars for even length, on a char for odd)
Expand outward while left/right match; track the best window
Take the longest over all centers
"""
"""
Time Complexity: O(n^2) in worst case (e.g., all same chars)
Space Complexity: O(1)
"""


class longestPalindromeSub:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        best_l = best_r = 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)       # odd-length center
            l2, r2 = expand(i, i + 1)   # even-length center
            if r1 - l1 > best_r - best_l:
                best_l, best_r = l1, r1
            if r2 - l2 > best_r - best_l:
                best_l, best_r = l2, r2

        return s[best_l:best_r + 1]

if __name__ == "__main__":
    obj = longestPalindromeSub()
    print(obj.longestPalindrome("babad"))    # "bab" or "aba"
    print(obj.longestPalindrome("cbbd"))     # "bb"
    print(obj.longestPalindrome("a"))        # "a"
    print(obj.longestPalindrome("ac"))       # "a" or "c"
    print(obj.longestPalindrome("aaaa"))     # "aaaa"