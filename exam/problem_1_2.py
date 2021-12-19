from collections import deque

firework_effects = [int(el) for el in input().split(', ')]
explosive_power = [int(el) for el in input().split(', ')]

firework_effects = deque(el for el in firework_effects if el > 0)
explosive_power = [el for el in explosive_power if el > 0]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
is_bombs = False
while firework_effects and explosive_power:
    first_el = firework_effects.popleft()
    second_el = explosive_power.pop()
    if first_el <= 0:
        firework_effects.popleft()
    if second_el <= 0:
        explosive_power.pop()
    sum_values = first_el + second_el
    if sum_values % 3 == 0 and sum_values % 5 != 0:
        palm_fireworks += 1
    elif sum_values % 3 != 0 and sum_values % 5 == 0:
        willow_fireworks += 1
    elif sum_values % 3 == 0 and sum_values % 5 == 0:
        crossette_fireworks += 1
    else:
        first_el -= 1
        firework_effects.append(first_el)
        explosive_power.append(second_el)
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        print("Congrats! You made the perfect firework show!")
        is_bombs = True
        break

if not is_bombs:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(el) for el in firework_effects)}")
elif explosive_power:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")