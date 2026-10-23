def add_bonus(scores, bonus=1):
    for i in range(len(scores)):
        scores[i] += bonus

grades = [2, 99, 5]
print(f"Before: {grades}")
add_bonus(grades)
print(f"After default bonus: {grades}")
add_bonus(grades,5)
print(f"After extra bonus: {grades}")


# Before: [2, 99, 5]
# After default bonus: [3, 100, 6]
# After extra bonus: [8, 105, 11]


# Если в функцию передается изменяемый тип данных то функция может изменять оригинал

# В том числе свли собственные объктыб которые создаются с помощью классов