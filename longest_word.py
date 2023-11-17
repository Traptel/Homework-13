def longest_words(file):
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    max_length = max(len(word) for word in words)
    long_words_list = [word for word in words if len(word) == max_length]

    return long_words_list


longest_words_list = longest_words("article.txt")
print("Найдовші слова:", ", ".join(longest_words_list))
