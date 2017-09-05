class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1 or len(s) == 0: return s

        # init:
        str = ['&', '#']
        for i in s:
            str += [i, '#']
        str.append('*')
        id = mx = 0
        p = [1] * len(str)

        # Manacher algorithm
        for i in range(1, len(str) - 1):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            while str[i + p[i]] == str[i - p[i]]:   p[i] += 1
            (mx, id) = (p[i] + i, i) if i + p[i] > mx else (mx, id)

        id = p.index(max(p))
        mx = max(p) + id
        return s[int((2 * id - mx) / 2): int((mx - 1) / 2)]
