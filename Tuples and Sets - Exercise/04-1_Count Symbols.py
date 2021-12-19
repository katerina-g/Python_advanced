text = input()

chars_count = {}

for ch in text:
    if ch not in chars_count:
        chars_count[ch] = 0
    chars_count[ch] += 1

for (char, count) in sorted(chars_count.items()):
    print(f"{char}: {count} time/s")