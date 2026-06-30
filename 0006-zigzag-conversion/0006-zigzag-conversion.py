class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1:
            return s

        rows = []

        for i in range(numRows):
            rows.append("")

        currentRow = 0
        goingDown = True

        for ch in s:

            rows[currentRow] = rows[currentRow] + ch

            if currentRow == 0:
                goingDown = True

            elif currentRow == numRows - 1:
                goingDown = False

            if goingDown:
                currentRow = currentRow + 1
            else:
                currentRow = currentRow - 1

        answer = ""

        for row in rows:
            answer = answer + row

        return answer