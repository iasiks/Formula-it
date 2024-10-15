numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index = 4
right_part = numbers[:index]
left_part = numbers[index + 1:]

sum_of_numbers = sum(right_part) + sum(left_part)
count_of_numbers = len(numbers)
average = sum_of_numbers / count_of_numbers

numbers[4] = average


print("Измененный список:", numbers)
