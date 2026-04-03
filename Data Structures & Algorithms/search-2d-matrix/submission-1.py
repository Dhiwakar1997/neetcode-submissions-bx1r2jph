class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top, btm = 0, ROW-1
        
        while top<=btm:
            m_row = (top+btm)//2
            if target > matrix[m_row][-1]:
                top = m_row+1
            elif target< matrix[m_row][0]:
                btm = m_row-1
            else:
                break
        
        if not top<=btm:
            return False
        
        row=(top+btm)//2
        l,r = 0, COL-1

        while l<=r:
            mid = (r+l)//2

            if target < matrix[row][mid]:
                r=mid-1
            elif target > matrix[row][mid]:
                l=mid+1
            else:
                return True
        return False