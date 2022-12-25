import sort
import timeit

print('Доступные методы сортировки:');
print('  1 - Быстрая     2 - Расчёска');
print()
q = input('Введите название метода сортировки: ')
while q not in('Быстрая','быстрая','Расчёска','расчёска'):
    q = input('Данный метод не поддерживается программой, введите поддерживаемый метод сортирови: ')
print()

x=int(input('Введите количество чисел в массиве: '))
a=[0]*x
print()
for i in range(x):
    print('Введите число', i+1 ,'элемента массива:')
    a[i]=int(input())
print(); print('Задан массив:', a); print()

set_up='''sort.sr(a)'''
set_up1='''sort.rs(a)'''

if q in ('Быстрая','быстрая'):
    print('Результат быстрой сортировки:'); print(sort.sr(a)); print()
    print('Время затраченное на выполнение программы:', timeit.timeit(setup=set_up, number=100000, globals=globals()))

if q in ('Расчёска','расчёска'):
    print('Результат сортировки методом "Расчёска":'); print(sort.rs(a)); print()
    print('Время затраченное на выполнение программы:', timeit.timeit(setup=set_up, number=100000, globals=globals()))