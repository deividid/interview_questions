import time


def search_value(aray, value):
    if value in aray:
        return f'{value} is in the list.'

    return f'{value} is not in the list.'


devices = ["iphone", "android", "radio", "tv", "tablet", "pc", "laptop"] # list search time is O(n)

devices_optimize = set(devices) # with set the search time will be O(1)

input_value = input()

start = time.time()
result = search_value(devices_optimize, input_value)
end = time.time()

print(result)
print(f"Time to run check: {end - start}")

