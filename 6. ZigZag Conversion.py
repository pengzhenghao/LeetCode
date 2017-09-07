class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "" or numRows <= 1: return s
        d = 2 * numRows - 2
        cal = lambda k: int(k / d) * 2 + int(k % d / numRows)
        M = [['#'] * (cal(len(s) - 1) + 1) for _ in range(numRows)]
        for ind, char in enumerate(s):
            y = cal(ind)
            x = (d - ind % d) if y % 2 == 1 else (ind % d)
            M[x][y] = char
        return ''.join([item for rows in M for item in rows if item != '#'])
        
        
        # The best solution in the internet
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
