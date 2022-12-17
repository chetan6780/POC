path = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]
path = path[::-1]
path = [x for x in path if x != 0]
print(path)
