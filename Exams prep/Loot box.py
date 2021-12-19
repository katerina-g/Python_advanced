from collections import deque

first_loot_box = deque(int(el) for el in input().split())
second_loot_box = [int(el) for el in input().split()]

sum_items = 0

while first_loot_box and second_loot_box:
    first_el = first_loot_box.popleft()
    second_el = second_loot_box.pop()
    if (first_el + second_el) % 2 == 0:
        sum_items += (second_el + first_el)
    else:
        first_loot_box.appendleft(first_el)
        first_loot_box.append(second_el)
if len(first_loot_box) == 0:
    print("First lootbox is empty")
elif len(second_loot_box) == 0:
    print("Second lootbox is empty")
if sum_items >= 100:
    print(f"Your loot was epic! Value: {sum_items}")
else:
    print(f"Your loot was poor... Value: {sum_items}")