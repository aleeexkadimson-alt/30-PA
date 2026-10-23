def to_minutes(hours, minutes):
    total_minutes = hours * 60 + minutes
    return total_minutes

lesson_1_m = int(input("First lesson minutes:"))
lesson_2_m = int(input("Second lesson minutes:"))
lesson_1_h = int(input("First lesson hours:"))
lesson_2_h = int(input("Second lesson hours:"))

total_minutes_1 = to_minutes(lesson_1_h, lesson_1_m)
total_minutes_2 = to_minutes(lesson_2_h, lesson_2_m)

if total_minutes_1 > total_minutes_2:
    print("The first lesson is longer")
else:
    print("The second lesson is longer")