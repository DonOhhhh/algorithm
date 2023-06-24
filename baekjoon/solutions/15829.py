input()
s = input()
print(sum([((ord(c) - 96) * 31**i) for i, c in enumerate(s)]) % 1234567891)
