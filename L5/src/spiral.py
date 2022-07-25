def spiral(matrix):
        m, n = len(matrix), len(matrix[0])
        direction = 1
        i, j = 0, -1
        output = []
        while m * n > 0:
            for _ in range(n):
                j += direction
                output.append(matrix[i][j])
            m -= 1
            for _ in range(m):
                i += direction
                output.append(matrix[i][j])
            n -= 1
            direction *= -1
        return output


print(spiral([[1,2,3],[4,5,6],[7,8,9]])) # -> [1,2,3,6,9,8,7,4,5]
print(spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # -> [1,2,3,4,8,12,11,10,9,5,6,7]
