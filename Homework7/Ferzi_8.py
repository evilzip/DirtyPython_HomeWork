# На шахматной доске расположить 8 ферзей так, чтобы они не били друг друга
# приложить хотя бы один вариант такой расстановки
import random

list_squares_full = [[h,v] for h in range(1,9) for v in range(1,9)]

def dioganal_squares(position: [int, int]) -> list:
    # функция выдает координаты диагональных клеток которые поражаются ферзем стоящим на поле position
    diagonal_list = []
    i=position[0]
    j = position[1]
    while 0 < i < 8 and 0 < j < 8:
        i+=1
        j+=1
        diagonal_list.append([i,j])
    i = position[0]
    j = position[1]
    while 1<i<9 and 1<j<9:
        i-=1
        j-=1
        diagonal_list.append([i,j])
    i = position[0]
    j = position[1]
    while 0<i<8 and 1<j<9:
        i+=1
        j-=1
        diagonal_list.append([i,j])
    i = position[0]
    j = position[1]
    while 1<i<9 and 0<j<8:
        i-=1
        j+=1
        diagonal_list.append([i,j])
    return diagonal_list
def ferz_kill_zone( ferz_position: [int, int], current_desk: list ) -> list:
    # функция заменяет на [0,0] координаты тех клеток  доски которые поражаются ферзем на клетке ferz_position
    list1 = []
    list1 = list(filter(lambda x: x[0] == ferz_position[0], current_desk))
    list1 = list1 + list(filter(lambda x: x[1] == ferz_position[1], current_desk))
    list1 = list1 + list(filter(lambda x: x in dioganal_squares(ferz_position), current_desk))
    for i in range(len(current_desk)):
        if current_desk[i] in list1:
            current_desk[i] = [0,0]
    return current_desk

def convert_solution_to_chess_format(solution:list)->tuple:
    # преобразование решения (= список позиций всех 8ми ферзей в моих цифровых координатах) в шахматный язык
    solution_list = []
    letters = {1:'A',2:'B',3:'C',4:'D',5:'E', 6:'F', 7:'G', 8:'H'}
    for i in range(len(solution)):
        solution_list.append((letters.get(solution[i][1]))+str(9 - solution[i][0]))
    return tuple(sorted(solution_list))


file = open('Ferzi_solutions.txt', 'w') # очистка файла решений перед записью
file.close()

file = open('Ferzi_solutions.txt', 'a', encoding='UTF-8') # запись в файл искомых комбинаций решений


current_ferz_amount=0
remain_squares = [[h,v] for h in range(1,9) for v in range(1,9)]
position_ferz = [] # искомая комбинация ферзей
solutions_list= [] # список всех решений


while len(solutions_list)<92: # тут было условие бесконечно цикла, пока опытным путем не нашел что решений 92
    current_ferz_amount=0
    while current_ferz_amount<8:
        h = random.randint(1,8) # h,v - рандомно помещаем ферзя на доску
        v = random.randint(1,8) 
        if remain_squares[(h - 1) * 8 + v - 1] != [0, 0]: # проверям, поставили ли мы нового ферзя на уже битое поле [0,0]
            current_ferz_amount= current_ferz_amount + 1 # если нет - то плюсуем ферзя у уже найденным
            remain_squares = ferz_kill_zone([h, v], remain_squares) # помечаем клетки которые бъет этот ферзь
            #print(h, v,'Yes!', current_ferz_amount)
            position_ferz.append([h,v]) # добавляем позицию ферзя в список решения
        elif current_ferz_amount>5 and max(remain_squares)!= [0, 0]: # блок поиска новой позиции ферзя когда ферзей уже
            # больше пяти. Так чаще быстрее чем рандомом перебирать
            for hh in range(1, 8):
                for vv in range(1, 8):
                    if remain_squares[(hh - 1) * 8 + vv - 1] != [0, 0]:
                        current_ferz_amount = current_ferz_amount + 1
                        remain_squares = ferz_kill_zone([hh, vv], remain_squares)
                        # print(hh, vv,'!Yes', current_ferz_amount)
                        position_ferz.append([hh, vv])
        elif max(remain_squares) == [0, 0]: # постоянная проверка, что на доске еще есть место куда ставить ферзи
            # если все клетки под боем а ферзей меншье 8, то все начинаем заново
            remain_squares = [[h,v] for h in range(1,9) for v in range(1,9)]
            position_ferz.clear()
            # print('RESET') видно в консоли когда комбинация 8 ферзей не собралась и начинается новый подбор
            current_ferz_amount=0
        # print(current_ferz_amount, 'k')
    if convert_solution_to_chess_format(position_ferz) not in solutions_list:
        file.write(','.join(convert_solution_to_chess_format(position_ferz))+'\n')
        solutions_list.append(convert_solution_to_chess_format(position_ferz))
file.close()
# print(solutions_list)