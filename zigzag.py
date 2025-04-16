def convert(s: str, numRows: int):
    matrix = []
    for i in range(numRows):
        matrix.append([])

    top = True
    count = 0

    for letter in s:
        if top:
            if count < numRows:
                matrix[count].append(letter)
                count += 1

            else:
                top = False
                count -= 2

        if not top:
            if count == 0:
                top = True
                matrix[count].append(letter)
                count += 1

            else:
                matrix[count].append(letter)
                count -= 1

    result = ''
    for row in matrix:
        result += ''.join(row)

    return result


word = input()
rows = int(input())

print(convert(word, rows))

