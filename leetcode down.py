
class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(self.n+1)  # 1-indexed

    def init(self, init_val):
        for i, v in enumerate(init_val):
            self.add(i, v)

    def add(self, i, x):
        # i: 0-indexed
        i += 1  # to 1-indexed
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

    def sum(self, i, j):
        # return sum of [i, j)
        # i, j: 0-indexed
        return self._sum(j) - self._sum(i)

    def _sum(self, i):
        # return sum of [0, i)
        # i: 0-indexed
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & (-i)
        return res

    def lower_bound(self, x):
        s = 0
        pos = 0
        depth = self.n.bit_length()
        v = 1 << depth
        for i in range(depth, -1, -1):
            k = pos + v
            if k <= self.n and s + self.bit[k] < x:
                s += self.bit[k]
                pos += v
            v >>= 1
        return pos

    def __str__(self):  # for debug
        arr = [self.sum(i, i+1) for i in range(self.n)]
        return str(arr)


class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        topos1 = {}
        for i, a in enumerate(nums1):
            topos1[a] = i
        bit = BIT(n+1)
        L = [0]*n
        for i, a in enumerate(nums2):
            L[i] = bit.sum(0, topos1[a])
            bit.add(topos1[a], 1)
        bit = BIT(n+1)
        R = [0]*n
        for i in range(n-1, -1, -1):
            a = nums2[i]
            R[i] = bit.sum(topos1[a], n)
            bit.add(topos1[a], 1)
        # print(L)
        # print(R)
        ans = 0
        for i in range(n):
            ans += L[i]*R[i]
        return ans
