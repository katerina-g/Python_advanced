from collections import deque

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]

bombs = False
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while firework_effects and explosive_power:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    both_power = firework_effects[0] + explosive_power[-1]
    if both_power % 3 == 0 and both_power % 5 != 0:
        palm_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif both_power % 3 != 0 and both_power % 5 == 0:
        willow_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif both_power % 3 == 0 and both_power % 5 == 0:
        crossette_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        firework_effects.rotate(-1)
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        bombs = True
        break

if bombs:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")

