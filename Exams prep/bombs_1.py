from collections import deque

d_b = 40
ch_b = 60
s_d_b = 120

bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = list(map(int, input().split(', ')))

d_b_count = 0
ch_b_count = 0
s_d_b_count = 0
is_bombs = False
while bomb_effects and bomb_casings:
    if d_b_count >= 3 and ch_b_count >= 3 and s_d_b_count >= 3:
        is_bombs = True
        break
    sum_values = bomb_effects[0] + bomb_casings[-1]
    if sum_values == d_b:
        d_b_count += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum_values == ch_b:
        ch_b_count += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum_values == s_d_b:
        s_d_b_count += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if is_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {ch_b_count}")
print(f"Datura Bombs: {d_b_count}")
print(f"Smoke Decoy Bombs: {s_d_b_count}")