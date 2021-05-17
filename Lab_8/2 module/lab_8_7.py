# 7. Створіть словник з рядка 'pythonist' наступним чином: в якості ключів
# використовуйте символи рядка, а в якості значень - кількість входжень даного
# символа.

word = "pythonist"

dictionary = {k: word.count(k) for k in word}

print(dictionary)