text = input()

VOWELS = {'a', 'o', 'u', 'e', 'i'}
[VOWELS.add(x.upper()) for x in list(VOWELS)]

result = [ch for ch in text if ch not in VOWELS]

print(''.join(result))