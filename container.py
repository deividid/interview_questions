def container(height):
    start = 0
    end = len(height) - 1
    max_container = 0
    while start < end:
        area = min(height[start], height[end]) * (end - start)
        if area > max_container:
            max_container = area

        if height[start] < height[end]:
            start += 1

        else:
            end -= 1

    return max_container


data = [int(d) for d in input().split(', ')]

result = container(data)

print(result)
