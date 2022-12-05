list = [2, 3, 5, 9, 3]
summ = 0
for i in range(1, len(list), 2):
        summ += list[i]       
print(f"{list} -> сумма элементов на нечётных позициях: {summ}")