from collections import deque


def fill_the_box(h, l, w, *args):
    h = int(h)
    l = int(l)
    w = int(w)
    box = h * l * w
    cubes = 0
    cubes_list = deque()
    for i in range(len(args)):
        if args[i] == "Finish":
            break
        else:
            cube = int(args[i])
            cubes += cube
            cubes_list.append(cube)
    for _ in range(len(cubes_list)):
        first_cube = int(cubes_list.popleft())
        if first_cube <= box:
            box -= first_cube

        else:
            first_cube -= box
            cubes_list.append(first_cube)
            return f"No more free space! You have {sum(cubes_list)} more cubes."

    return f"There is free space in the box. You could put {box} more cubes."




print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))