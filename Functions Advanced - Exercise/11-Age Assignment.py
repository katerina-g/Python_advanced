def age_assignment(*names, **kwargs):
    assignment = {}
    for name in names:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                assignment[name] = age
    return assignment


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))