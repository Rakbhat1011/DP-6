"""
Build the sequence in ascending order; start with ugly[0] = 1
Maintain three indices i2, i3, i5 pointing to the next candidates multiplied by 2, 3, 5
At each step, pick the minimum of (2*ugly[i2], 3*ugly[i3], 5*ugly[i5]), append it, and advance all pointers that match this minimum (to avoid duplicates)
"""
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


class uglyNumbers:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0

        while len(ugly) < n:
            n2, n3, n5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            nxt = min(n2, n3, n5)
            ugly.append(nxt)
            if nxt == n2: i2 += 1
            if nxt == n3: i3 += 1
            if nxt == n5: i5 += 1

        return ugly[-1]

if __name__ == "__main__":
    obj = uglyNumbers()
    print(obj.nthUglyNumber(1))   # 1
    print(obj.nthUglyNumber(10))  # 12
    print(obj.nthUglyNumber(15))  # 24
    print(obj.nthUglyNumber(150)) # 5832


