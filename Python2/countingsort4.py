words = [tuple(raw_input().split()) for _ in range(input())]
words = sorted([(int(y), z if x * 2 >= len(words) else '-') for x, (y, z) in enumerate(words)], key=lambda x: x[0])
print ' '.join([y for x, y in words])