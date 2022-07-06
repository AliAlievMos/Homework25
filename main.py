
menu = '♘ ♞ ♘ ♞ ♘ ♞\n___МЕНЮ___\n1)ввести данные\n2)выход'
chessboard = '8▓░▓░▓░▓░\n\
7░▓░▓░▓░▓\n\
6▓░▓░▓░▓░\n\
5░▓░▓░▓░▓\n\
4▓░▓░▓░▓░\n\
3░▓░▓░▓░▓\n\
2▓░▓░▓░▓░\n\
1░▓░▓░▓░▓\n\
 abcdefgh'

# создал словарь присвоил каждой координате уникальное значение по порядку,
# а затем установил, что если разница между значением начальной и конечной координаты
# равна одному из этих чисел(17,15,10,6,-6,-10,-15,-17), то конь может пойти на эту клетку

i1 = 0
A = []
for i in range(64):
    A.append(i1)
    i1 += 1
B = []
num ='12345678'
letters ='abcdefgh'
for i in range(8):
    for i1 in range(8):
        B.append(f'{letters[i]}{num[i1]}')

C = dict(zip(B, A))
print(C)
print(63+1 == 65 - 1)





while True:
    print(menu)
    a = input()
    if a == '1':
        print(chessboard)
        print('Введите начальные координаты коня(в формате "h8")')
        start = input()
        print('Введите конечные координаты коня(в формате "h8")')
        finish = input()
        diff = C[start] - C[finish]
        if diff == 17 or diff == 15 or diff == 10 or diff == 6 or \
                diff == -6 or diff == -10 or diff == -15 or diff == -17:
            print(True)
        else:
            print(False)
    if a == '2':
        print('Выхожу')
        break
