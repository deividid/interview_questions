def longestPalindrome(s: str) -> str:

    def expand(s, left, right):
        if s == '':
            return s
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

    start = 0
    end = 0

    for i in range(len(s)):
        odd = expand(s, i, i)
        even = expand(s, i, i + 1)
        best_option = max(odd, even)

        if best_option > end - start:
            start = i - (best_option - 1) // 2
            end = i + best_option // 2

    return s[start:end+1]

word = input()

print(longestPalindrome(word))