#!/usr/bin/env python
# coding: utf-8

# In[1]:


8 / 13


# In[2]:


8//13
# // - возвращает целую часть от частного


# In[3]:


8%13


# In[4]:


11 % 8
# % - возвращает остаток от деления


# In[5]:


2014**14
# ** - возведение в степень


# In[6]:


0.1 + 0.1 + 0.1


# In[7]:


0.1 + 0.1 + 0.1 + 0.3 + 0.3


# In[8]:


2014.0 ** 14


# In[9]:


7 / 3


# In[10]:


7.0 // 3.0


# In[11]:


int(2.99)


# In[12]:


int(-(1.6))


# In[13]:


9**19 - int(float(9**19))


# In[14]:


type(-1)


# In[15]:


type(1.806477376560755e+46)


# In[16]:


a = 100
a -= 10


# In[17]:


print(a)


# In[18]:


s = input()


# In[ ]:


d = input()


# In[ ]:


print (d, s)


# In[ ]:


print ('Hello!')
name = input('Enter your name: ')
surname = input('Enter your surname: ')
print ('How are you, Mr.', name, surname, '?')


# In[ ]:


T = int(input())
h = T // 60
m = T - h * 60
print(h)
print(m)


# In[149]:


X = int(input('Total sleep in minutes: '))
H = int(input('Sleep hours: '))
M = int(input('Sleep minutes: '))
print('Allarm time: ', (H + X // 60 + int((M + X % 60) / 60)), ':', (int(M + X % 60) - 60 * int((M + X % 60) / 60)))


# In[ ]:


-5 < 100


# In[ ]:


5 == 2 + 3


# In[ ]:


x = int(input())
print(10 <= x <= 99)


# In[ ]:


s, d = 110, 70
print ((s - d) / s)


# In[ ]:


((a and b) or ((not a) and (not b)))


# In[ ]:


x = 5
y = 10
y > x * x or y >= 2 * x and x < y


# In[ ]:


a = True
b = False
a and b or not a and not b
# приоритеты - сначала NOT,потом AND, затем только OR


# In[ ]:


z = int(input())
if z % 2 == 0:
    print('z - четное число')
else:
    print('z - нечетное число')


# In[ ]:


z = int(input())
if z < 0:
    print('z - отрицательное число')
elif z == 0:
    print('z - ноль')
else:
    print('z - положительное число')


# In[ ]:


a = int(input())
b = int(input())
if b != 0:
    print(a / b)
else:
    print ('Требуется ввести ненулевое значение b')
    b = int(input())
    if b == 0:
        print('Неудачная попытка')
    else:
        print(a / b)


# In[ ]:


A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print('Это нормально')
elif A > H:
    print('Недосып')
else:
    print('Пересып')


# In[ ]:


A = int(input())
if A % 400 == 0:
    print('Високосный')
elif A % 4 == 0 and A % 100 != 0:
    print('Високосный')
else:
    print('Обычный')


# In[ ]:


'abra' + 'kadabra'


# In[ ]:


'variable_0999' < 'variable_1'


# In[20]:


print('1st string','\n\nLast string')
# здесь \n - символ перевода строки


# In[150]:


a = 'abra'
b = 'cadabra'
print(a, b)
print(a + b)


# In[ ]:


'123' + '42'


# In[ ]:


"123" + "42"


# In[ ]:


a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
print((p * (p - a) * (p - b) * (p - c)) ** 0.5)


# In[ ]:


# (−15,12]∪(14,17)∪[19,+∞)
a = int(input())
if 12 >= a > (-(15)):
    print('True')
elif 14 < a < 17:
    print('True')
elif a >= 19:
    print('True')
else:
    print('False')


# In[ ]:


a = float(input())
b = float(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == 'pow':
    print(a ** b)
elif c == '/' and b != 0:
    print(a / b)
elif c == 'mod' and b != 0:
    print(a % b)
elif c == 'div' and b != 0:
    print(a // b)
else:
    print('Деление на 0!')


# In[ ]:


x = input()
if x == 'круг':
    r = float(input())
    print(3.14 * r ** 2)
elif x == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif x == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) * 0.5
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)


# In[ ]:


a = int(input())
b = int(input())
c = int(input())
if a >= b and b >= c:
    print(a)
    print(c)
    print(b)
elif a >= c and c >= b:
    print(a)
    print(b)
    print(c)
elif b >= a and a >= c:
    print(b)
    print(c)
    print(a)
elif b >= c and c >= a:
    print(b)
    print(a)
    print(c)
elif c >= a and a >= b:
    print(c)
    print(b)
    print(a)
elif c >= b and b >= a:
    print(c)
    print(a)
    print(b)


# In[ ]:


a = int(input())
if a % 10 == 1 and a % 100 != 11:
    print(a, 'программист')
elif a % 10 == 2 and a % 100 != 12 or a % 10 == 3 and a % 100 != 13 or a % 10 == 4 and a % 100 != 14:
    print(a, 'программиста')
else:
    print(a, 'программистов')


# In[ ]:


a,b,c,d,e,f = input()
if int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
    print('Счастливый')
else:
    print('Обычный')


# In[30]:


systolic = int(input('Systolic pressure: '))
diastolic = int(input('Diastolic pressure: '))
if systolic <= diastolic:
    print('Incorrect input')
else:
    def pulse_press_var(systolic,diastolic):
        return systolic - diastolic
    print ('Pulse pressure:', pulse_press_var(systolic,diastolic))
    pulse_pressure = pulse_press_var(systolic,diastolic)
    
    def mabp_var(systolic,diastolic):
        return diastolic + (systolic - diastolic) /3
    print ('MABP:', mabp_var(systolic,diastolic))
    MABP = mabp_var(systolic,diastolic)
    
    def pulse_pressure_c(systolic,diastolic):
        if (systolic - diastolic) < 35:
            return 0
        elif 35 <= (systolic - diastolic) < 40:
            return 1
        elif 40 <= (systolic - diastolic) <= 45:
            return 2
        elif 45 <= (systolic - diastolic) <= 60:
            return 3
        else:
            return 4
    print('Pulse pressure CLASS:', pulse_pressure_c(systolic,diastolic))
    pulse_pressure_class = pulse_pressure_c(systolic,diastolic)
    
    def mabp_c(systolic,diastolic):
        if (diastolic + (systolic - diastolic) / 3) < 79.9:
            return 0
        elif 79.9 <= (diastolic + (systolic - diastolic) / 3) < 99.1:
            return 1
        else:
            return 2
    print('MABP CLASS:', mabp_c(systolic,diastolic))
    MABP_class = mabp_c(systolic,diastolic)
    
    def blood_pressure_opinion(systolic,diastolic,MABP,MABP_class,pulse_pressure,pulse_pressure_class):
        if MABP_class == 2 or pulse_pressure_class == 4:
            return 1
        if MABP_class > 0 and pulse_pressure_class == 0:
            return 4       
        if MABP_class == 0 and pulse_pressure_class == 0 and pulse_pressure / systolic < 0.25:
            return 2
        if MABP_class == 1 and diastolic > 89 or MABP_class == 1 and systolic > 129:
            return 3
        if (MABP_class ==1 and systolic < 120 and diastolic < 80 and pulse_pressure_class == 2 or 
                MABP_class ==1 and systolic < 120 and diastolic < 80 and pulse_pressure_class == 1):
            return 12    
        if MABP_class == 0 and pulse_pressure_class == 2:
            return 11
        if MABP_class == 0 and pulse_pressure_class == 1:
            return 11
        if (MABP_class == 1 and systolic == 120 and diastolic == 80 and pulse_pressure_class == 2 or
                MABP_class == 1 and systolic == 120 and diastolic == 80 and pulse_pressure_class == 1):
            return 10    
        if MABP_class == 1 and systolic <= 129 and diastolic <= 84 and pulse_pressure_class == 2:
            return 9 
        if MABP_class == 1 and systolic <= 129 and diastolic <= 84 and pulse_pressure_class == 1:
            return 9 
        if MABP_class == 0 and pulse_pressure_class == 0 and pulse_pressure / systolic >= 0.25:
            return 7   
        if MABP_class == 0 and pulse_pressure_class == 3:
            return 8    
        if MABP_class == 1 and 84 < diastolic <= 89:
            return 5      
        if MABP_class == 1 and systolic <= 129 and diastolic <= 84 and pulse_pressure_class == 3:
            return 6
        return 100
    print('Blood pressure opinion:', blood_pressure_opinion(systolic,diastolic,MABP,MABP_class,pulse_pressure,pulse_pressure_class))


# In[42]:


a = 10
while a > 0:
    print(a, end=' ') # end=' ' указывает, что вывод след. рез-та не с новой строки, а через пробел
    a -= 1 # уменьшается каждый раз на 1


# In[19]:


systolic = int(input('Systolic pressure: '))
diastolic = int(input('Diastolic pressure: '))
if systolic <= diastolic:
    print('Incorrect input')
elif 40 > systolic or systolic > 280 or 30 > diastolic or diastolic > 160:
    print('Out of range')


# In[ ]:


systolic = 40
diastolic = 30
while systolic > 45:
    def pulse_press_var(systolic,diastolic):
        return systolic - diastolic
        print (systolic, diastolic, pulse_press_var(systolic,diastolic))   


# In[22]:


a = 5
while a <= 100:
    if a % 5 == 0:
        print(a, end=', ')
    a += 1


# In[31]:


n = int(input())
c = 1
while c <= n:
    print('*' * c)
    c += 1


# In[128]:


n = int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'


# In[34]:


s = 0
i = int(input())
while i <= 5:
    s += i
    i += 1
print(s)


# In[44]:


summ = 0
b = 1
while b != 0:
    b = int(input())
    summ = summ + b
print(summ)


# In[64]:


a = int(input())
b = int(input())
d = max(a, b)
while d % a != 0 or d % b != 0:
    d += 1
print(d)


# In[68]:


i = 0
while i < 2:
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a * b)
    i += 1


# In[77]:


i=0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    if a == 0 or b == 0:
        continue # если подставить break, то будет по другому идти расчет
    print (a * b)
    i += 1


# i = 0
# s = 0
# while i < 10:
#     print('i(0)=', i)
#     i = i + 1
#     print('i(1)=', i)
#     s = s + i
#     print('s=', s)
#     if s > 15:
#         print('c > 15')
#         continue
#     i = i + 1
#     print('i(2)=', i)

# In[125]:


x = 0
while x <= 100:
    x = int(input())
    if x < 10:
        continue
    if x > 100:
        break
    print(x)


# In[124]:


x = 0
while x <= 100:
    x = int(input())
    if x < 10:
        continue
    print(x)


# In[127]:


for y in -2, -1, 0, 1, 2:
    print (y * y)


# In[4]:


for z in range(10):
    print (z ** 0.5)
# функция range передает начиная с 0 (0, 1,...9)


# In[3]:


float(-27.0)


# In[4]:


type(-27.0)


# In[6]:


type('aad')


# In[9]:


for i in range(15,21):
    print (i)
# шаг не задан, по умолчанию 1


# In[10]:


for j in range(5,25,5):
    print (j)
# шаг задан


# In[11]:


print('*' * 3)


# In[14]:


n = int(input())
for i in range(n):
    print('*' * n)


# In[18]:


n = int(input())
for i in range(n):
    for j in range(n*3):
        print('*', end='')
    print()


# In[47]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i1 in range(c, d + 1):
    print('\t', i1, end='')
for i2 in range(a, b + 1):
    print()
    print(i2, end='')
    for i3 in range(c, d + 1):
        print('\t', i2 * i3, end='')


# In[51]:


#Суммируются все нечетные числа в интервале от а до b (вариант 1)
a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print(s)


# In[56]:


#Суммируются все нечетные числа в интервале от а до b (вариант 2 - проверка на четность вынесена за пределы цикла)
a, b = input().split()
a = int(a)
b = int(b)
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)


# In[57]:


#Суммируются все нечетные числа в интервале от а до b (вариант 3 - ввод исх. данных по-другому)
a, b = (int(i) for i in input().split())
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)


# In[97]:


#Вывод среднего арифметического от всех чисел, кратных 3, из интервала введенных начального и конечного a и b
a, b = (int(i) for i in input().split())
s = 0
y = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        y += 1
print(s / y)


# In[99]:


#Подсчет числа встречающихся в строке символов 'c'
word = input()
cnt = 0
for letter in word:
    if letter == 'c':
        cnt += 1
print(cnt)


# In[100]:


#Подсчет числа встречающихся в строке символов 'c' (альтернативный вариант с применением метода count к строковому объекту)
word = input()
print(word.count('c'))


# In[103]:


#Строковые методы
    # 1. Замена всех символов на заглавные (саму строковую переменную string метод не меняет)
string = 'AbdDcc'
result = string.upper()
print(result)


# In[104]:


#Строковые методы
    # 2. Замена всех символов на строчные (саму строковую переменную string метод не меняет)
string = 'AbdDcc'
result = string.lower()
print(result)


# In[107]:


#Строковые методы
    # 3. Число вхождений подстроки в строку
string = 'AbdDcc1cc0'
substring = 'cc'
result = string.count(substring)
print(result)


# In[108]:


#Строковые методы
    # 4. Порядковый номер (начиная с 0) первого вхождения подстроки в строку
string = 'AbdDcc1cc0'
substring = 'cc'
result = string.find(substring)
print(result)


# In[109]:


string = 'AbdDcc1cc0'
substring = 'cС'
result = string.find(substring)
print(result)
# Если нет ни одного вхождения подстроки, то возвращается -1


# In[113]:


#Проверка факта наличия вхождения подстроки в строку
string = 'AbdDcc1cc0'
substring = 'cС'
if 'Cc' in string:
    print('yeah!') 
else: 
    print('no!')


# In[115]:


#Строковые методы
    # 5. Замена одних символов на другие (саму строковую переменную string метод не меняет)
string = 'AbdDcc1cc0'
result = string.replace('c', 'S')
print(result)


# In[116]:


#Последовательный вызов методов строковых
string = 'AbdDcc1cc0'
string.upper().count('Cc'.upper())


# In[130]:


#Вывод процента вхождения символов 'c' и 'g' в строке (регистронезависимый поиск)
string = input()
result = (int(string.lower().count('C'.lower())) + int(string.lower().count('G'.lower()))) / len(string) * 100
print(result)


# In[139]:


#Slicing - операции с диапазонами символов
d = 'ATTCGGAGCT'
#1
print('1. ', d[1]) #Вывод символа №1 (отсчет с 0)
#2
print('2. ', d[1:4]) #Вывод символов 1, 2, 3, 4 (отсчет с 0)
#3
print('3. ', d[:4]) #Вывод первых четырех символов
#4
print('4. ', d[4:]) #Вывод всех символов начиная с четвертого (включительно)
#5
print('5. ', d[-4:]) #Вывод последних четырех символов
#6
print('6. ', d[1:-1]) #Вывод всех символов начиная с №1 (включительно) до последнего (исключая последний)
#7
print('7. ', d[1:-1:2]) #Вывод символов начиная с №1 (включительно) до последнего (исключая последний) с шагом 2
#8
print('8. ', d[::-1]) #Вывод всех символов в обратном порядке


# In[151]:


#Группы одинаковых символов исходной строки ввода заменяются на этот символ и количество его повторений в этой позиции строки

st = input()
cnt = 0
for i in range(len(st)):
    if i < (len(st) - 1) and st[i] == st[i + 1]:
        cnt += 1
    elif i < (len(st) - 1) and st[i] != st[i + 1]:
        print(str(st[i]) + str(cnt + 1), end='')
        cnt = 0
    elif len(st) == 1:
        print(str(st[i]) + '1', end='')
        break
    elif i == (len(st) - 1) and st[i - 1] != st[i]:
        print(str(st[-1]) + '1', end='')
        cnt = 0
    elif i == (len(st) - 1) and st[i - 1] == st[i]:
        print(str(st[i]) + str(cnt + 1), end='')
    else:
        print(str(st[0]) + str(len(st)), end='')


# In[161]:


pulse_stream = [60, 65, 66, 61, 59]
for bpm in pulse_stream:
    print(bpm)


# In[164]:


params = ['bpm', 'sdnn', 'bmi', 'weight']
for i in params:
    print("user_id, " + i + ", timestamp")


# In[170]:


params = ['bpm', 'sdnn', 'bmi', 'weight']
print(len(params))
print(params[0])
print(params[:2])
print(params[::-2])


# In[171]:


params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params2 = ['пульс', 'сднн']
print(params1 + params2)


# In[174]:


params2 = ['пульс', 'сднн']
print(params2 * 3)


# In[177]:


#Замена элемента в списке
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1[3] = 'height'
print(params1)


# In[180]:


#Добавление элементов в список (вариант 1 - в конец)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1.append('spo2')
print(params1)


# In[181]:


#Добавление элементов в список (вариант 2 - в конец)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1 += ['spo2', 'bpm']
print(params1)


# In[182]:


#Добавление элементов в список (вариант 3 - в любую позицию)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1.insert(2, 'spo2')
print(params1)


# In[183]:


params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1 += 'spo2'
print(params1)


# In[186]:


#Удаление элементов из списка
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1.remove('weight')
print(params1)
del params1[1]
print(params1)


# In[188]:


#Поиск элементов в списке
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
if 'bmi' in params1:
    print(params1[2], 'in params')
if 'age' not in params1:
    print('age', 'is out')


# In[191]:


#Поиск элементов в списке по индексу
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
ind1 = params1.index('bpm')
print(ind1)
ind1 = params1.index('age') #такого элемента нет в списке, поэтому возвращается с ошибкой


# In[1]:


#Сортировка списка (вариант 1 - не изменяет исходный)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params2 = sorted(params1)
print(params2)


# In[2]:


#Сортировка списка (вариант 2 - изменяет исходный)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1.sort()
print(params1)


# In[7]:


params1 = ['bpm', 'sdnn', 'bmi', 'weight']
min_param = min(params1)
max_param = max(params1)
print(min_param, max_param)


# In[8]:


#Cортировка списка от конца (вариант 1)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1.reverse()
print(params1)


# In[14]:


#Cортировка списка от конца (вариант 2)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1[::-1]
print(params1)


# In[12]:


#Cортировка списка от конца (вариант 1)
params1 = ['bpm', 'sdnn', 'bmi', 'weight']
params1.reverse()
print(params1)


# In[15]:


a = [1, 2, 3]
b = a
print(b)

a[1] = 10
print(b)

b[0] = 20
print(a)

a = [5, 6]
print(b)


# In[16]:


#Генерация списков
a = [i * i for i in range(6)]
print(a)


# In[17]:


a = [int(i) for i in input().split()]


# In[17]:


# Суммируются все числа, введенные в строке
a = input().split()
b = 0
for i in range(len(a)):
    b += int(a[i])
print(b)


# In[19]:


# Выводит суммы двух соседних чисел для каждого числа из списка
a = input().split()
for i in range(len(a)):
    if len(a) == 1:
        print(int(a[i]))
    else:
        print(int(a[i-1]) + int(a[i - len(a) + 1]), end=' ')


# In[51]:


# Возвращает все уникальные числа из списка, которые повторяются хотя-бы 1 раз
b = input().split()
b.sort()
for i in range(1, len(b)):
    if i < len(b) - 1:
        if b[i] != b[i - 1]:
            continue
        elif b[i] == b[i - 1] and b[i] == b[i + 1]:
            continue
        else:
            print(int(b[i]), end=' ')
    else:
        if b[i] == b[i - 1]:
            print(int(b[i]), end=' ')


# In[ ]:


# Генерация таблиц
a = [[0] * n for i in range(n)]    # квадратная матрица (число строк = числу столбцов)
a = [[0 for i in range(n)] for j in range(p)]    # число строк и столбцов кастомизировано


# In[58]:


n = 4
p = 8
a = [[0 for i in range(n)] for j in range(p)]
a[6][3] = 155
print(a[6][3])
print(a[0][0])


# In[62]:


# Возвращает наименьшее из введенных чисел списка (аналогично функции min)
c = [int(i) for i in input().split()]
m = c[0]
for j in c:
    if m > j:
        m = j
print(m)


# In[76]:


# Сапёр
n, m, k = (int(i) for i in input().split())    # Ввод параметров массива (число строк, столбцов, кол-во мин)
a = [[0 for j in range(m)] for i in range(n)]  # Генерация массива n * m, заполненного нулями
for i in range(k):
    row, col = (int(i) - 1 for i in input().split()) # Чтение k пар чисел строка/столбец из ввода координат мин
    a[row][col] = -1                                 # Присвоение ячейкам с введенными координатами значения -1 (мина)
for i in range(n):            # Цикл перебора мин по
    for j in range(m):        # соседству с каждой ячейкой
        if a[i][j] == 0:              # Проверка, что данная ячейка не занята миной
            for di in range(-1, 2):        # Цикл перебора всех соседних ячеек
                for dj in range(-1, 2):    # со смещением 1 для данной ячейки
                    ai = i + di         # Координата соседней ячейки (в строке) со смещением di
                    aj = j + dj         # Координата соседней ячейки (в столбце) со смещением dj
                    if 0 <= ai < n and 0 <= aj < m  and a[ai][aj] == -1:     # Проверка, что данная ячейка попадает в пределы 
                        a[i][j] += 1                                       # массива и в ней мина (тогда переход к следующей)
for i in range(n):           # Цикл вывода 
    for j in range(m):       # карты мин
        if a[i][j] == -1:         # Если в ячейке мина, то
            print('*', end = '')  # выводим в ней *
        elif a[i][j] == 0:            # Если в ячейке нет мины и она не соседствует 
            print('.', end = '')      # с миной, то выводим в ней '.'   
        else:                 # Если ячейка соседствует с миной, то 
            print(a[i][j], end = '')    # выводим ее значение
    print()                                     # Перевод строки


# In[75]:


a


# In[125]:


a = [1, 3]
print(len(a))


# In[ ]:




