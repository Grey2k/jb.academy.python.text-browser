index = int(input().strip())

builtins = dir(locals()['__builtins__'])

print(builtins[index])
