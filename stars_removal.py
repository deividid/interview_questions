def removeStars(s: str) -> str:
    result = ''
    pos = len(s) - 1
    count = 0
    while pos >= 0:
        if s[pos] != '*':
            if count == 0:
                result += s[pos]

            else:
                count -= 1

        else:
            count += 1

        pos -= 1

    return result[::-1]


word = input()

print(removeStars(word))