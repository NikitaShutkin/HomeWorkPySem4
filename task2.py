# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты 
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число 
# ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних 
# с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один 
# заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

n = int(input('Введите колличество кустов: '))
s = list()
max=0
for i in range(n): 
    a = int(input(f'Введите колличество ягод на {i+1} кусте: ')) 
    s.append(a)
print(s)
for i in range(1, n-1):
    sum= s[i]+s[i-1]+s[i+1]
    if sum>max:
        max=sum
if s[0] + s[-1] + s[-2] > max:
	max = s[0] + s[-1] + s[-2]
if s[0] + s[1] + s[-1] > max:
	max = s[0] + s[1] + s[-1]  
print(f'Максимум ягод, что может собрать модуль: {max}')        
      

