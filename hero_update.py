def update_hero(**kwargs):
    with open("hero.ini", "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        for key, value in kwargs.items():
            if key in lines[i]:
                lines[i] = f"{key}={value}\n"

    with open("hero.ini", "w") as file:
        file.writelines(lines)


update_hero(hero="Halk", power=450, Y=2.3)
