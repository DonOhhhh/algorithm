num = sorted(list(map(int,input().split())))
gcd = num[0]
while gcd != 0 and (num[1]%gcd + num[0]%gcd):
	gcd -= 1
lcm = gcd * (num[1] // gcd) * (num[0] // gcd)
print(gcd)
print(lcm)