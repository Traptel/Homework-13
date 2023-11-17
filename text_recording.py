with open("input.txt", "w", encoding="utf-8") as file:
    while True:
        user_input = input("Введіть рядок (порожній рядок для завершення): ")
        if not user_input:
            break
        file.write(user_input + "\n")
