from collections import deque


firework_effects = deque([int(x) for x in input().split(", ") if int(x) > 0])
explosive_power = [int(x) for x in input().split(", ") if int(x) > 0]

fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}

show = False
while firework_effects and explosive_power:
    curr_firework = firework_effects[0]
    curr_explosive = explosive_power[-1]
    sum_effects = curr_firework + curr_explosive
    if curr_firework <= 0:
        firework_effects.popleft()
        continue
    elif curr_explosive <= 0:
        explosive_power.pop()
        continue
    if sum_effects % 3 == 0 and sum_effects % 5 != 0:
        fireworks["Palm Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_effects % 3 != 0 and sum_effects % 5 == 0:
        fireworks["Willow Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif sum_effects % 3 == 0 and sum_effects % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects.popleft())
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        show = True
        break
if show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
for key, value in fireworks.items():
    print(f"{key}: {value}")