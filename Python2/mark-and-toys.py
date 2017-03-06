__author__, K = "LaughDonor", int(raw_input().split()[1]),
for i, p in enumerate(sorted(map(int, raw_input().split()))):
	if K > p:
		K -= p
	else:
		break
print i