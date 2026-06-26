class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            ro=set()
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val not in ro :
                        ro.add(val)
                    else:
                        return False
        
        for i in range(9):
            co=set()
            for j in range(9):
                val = board[j][i]
                if val != ".":
                    if val not in co :
                        co.add(val)
                    else:
                        return False
        pos=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i,j in pos:
            s=set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    val = board[r][c]
                    if val !=".":
                        if val not in s:
                            s.add(val)
                        else:
                            return False
        return True