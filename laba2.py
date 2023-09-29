#Написать программу, которая читая файл, распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. 
#Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. 
#Распознование делать через регулярные выражения. В вариантах, где есть параметр К, К заменяется на любое число. нельзя.
#Натуральные числа. Выводит на экран только простые числа. Минимальное и максимальное число выводятся прописью.
import re 

primal = {'2': 'два', '3': 'три',  '5': 'пять',  '7': 'семь'}

with open('data.txt') as input_file:
    buffer = input_file.readline().split()
    print(buffer)

    max_min_array = []
    primal_row = ""
    pattern = r"\d+" 


    for i in range(0, buffer.__len__()):
        s = buffer[i]
        matches = re.findall(pattern, s)
        s1 = "".join(matches)
        
        for j in range(0, s1.__len__()):
            if (s1[j] == '2' or s1[j] == '3' or s1[j] == '5' or s1[j] == '7'):
                primal_row += s1[j]

        for q in range(0, primal_row.__len__()):

            if (primal_row[q] == '2' or primal_row[q] == '3' or primal_row[q] == '5' or primal_row[q] == '7'):
             max_min_array.append(int(primal_row[q]))

        if max_min_array:
            print('блок: ' + s1 + ' → ' + primal_row + "\nминимальное число: " +
                  primal[min(primal_row)] + "\nмаксимальное число: " + primal[max(primal_row)])
            print('\n')
            primal_row = ''
            max_min_array.clear()
            temp_row = ''
