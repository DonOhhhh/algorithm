n, m = map(int, input().split())
candidates = [input() for _ in range(n)]
vStr = [input() for _ in range(m)]
cnt = {name: 0 for name in candidates}
# 1. get valid strings
valid = list(filter(lambda x: x.replace(".", "") == "X", vStr))
# 2. count each candidates ballots
for s in valid:
    cnt[candidates[s.find("X")]] += 1
# 3. sort
candidates.sort(key=lambda x: -cnt[x])
# 4. get invalid strings
cnt["Invalid"] = m - len(valid)
# 5. print
for c in candidates:
    print(f"{c} {cnt[c] / m + 1e-9:.2%}")
print(f'Invalid {cnt["Invalid"] / m + 1e-9:.2%}')
