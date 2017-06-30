def col(W):
    return ord(W) - 65


class Excel(object):
    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.C = [[[0, [], []] for _ in range(col(W) + 1)] for _ in range(H)]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        cell = self.C[r - 1][col(c)]
        self._clear(cell, r, c)
        self._update(cell, v)

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        return self.C[r - 1][col(c)][0]

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        cell = self.C[r - 1][col(c)]
        self._clear(cell, r, c)
        celllist = []
        for s in strs:
            if len(s) == (2 or 3):
                celllist.append([int(s[1]) - 1, col(s[0])])
            else:
                a, b = s.split(':')
                celllist += [[i, j] for i in range(int(a[1:]) - 1, int(b[1:])) for j in range(col(a[0]), col(b[0]) + 1)]
        re = 0
        for ce in celllist:
            cell[2].append([ce[0], ce[1]])
            re += self.C[ce[0]][ce[1]][0]
            self.C[ce[0]][ce[1]][1].append([r - 1, col(c)])
        self._update(cell, re)
        return re

    def _clear(self, cell, r, c):
        if len(cell[2]):
            for i, j in cell[2]:
                if (r - 1, col(c)) in self.C[i][j][1]:
                    self.C[i][j][1].remove((r - 1, col(c)))
            cell[2] = []

    def _update(self, cell, val):
        cell[0] = val
        if cell[1] == []:    return
        for ce in cell[1]:
            ce = self.C[ce[0]][ce[1]]
            if len(ce[2]):
                re = 0
                for i, j in ce[2]:
                    re += self.C[i][j][0]
                self._update(ce, re)

                # Your Excel object will be instantiated and called as such:
                # obj = Excel(H, W)
                # obj.set(r,c,v)
                # param_2 = obj.get(r,c)
                # param_3 = obj.sum(r,c,strs)

