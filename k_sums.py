def max_k_sums(nums, k):
    seen = {}
    count = 0
    for n in nums:
        if n > k:
            continue
        if n in seen:
            count += 1
            if seen[n] > 1:
                seen[n] -= 1

            else:
                seen.pop(n)

        else:
            if k - n not in seen:
                seen[k - n] = 1

            else:
                seen[k - n] += 1

    return count


data = [int(d) for d in input().split(', ')]
lookup_number = int(input())

print(max_k_sums(data, lookup_number))
