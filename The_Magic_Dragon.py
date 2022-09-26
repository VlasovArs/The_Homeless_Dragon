def find_island(dragon_y, dragon_x): # Функция находит координаты ближайшего острова
    global island_y, island_x
    min_distance = lines * columns
    for y in range(lines):
        for x in range(columns):
            if board[y][x] == 1:
                distance_island = ((dragon_y - y) ** 2 + (dragon_x - x) ** 2) ** (1 / 2)
                if min_distance > distance_island:
                    min_distance = distance_island
                    island_y = y
                    island_x = x
    return island_y, island_x

global visited
def find_count_island(board ,island_y ,island_x): # Функция находит размер острова
    global size_island    # Количество участков суши
    visited.append([island_y, island_x])
    if island_y + 1 < lines and [island_y + 1, island_x] not in visited and board[island_y + 1][island_x] == 1:
        size_island += 1
        find_count_island(board, island_y + 1, island_x)
    if island_y - 1 >= 0 and ([island_y - 1, island_x]) not in visited and board[island_y - 1][island_x]:
        size_island += 1
        find_count_island(board, island_y - 1, island_x)
    if island_x + 1 < columns and [island_y, island_x + 1] not in visited and board[island_y][island_x + 1]:
        size_island += 1
        find_count_island(board, island_y, island_x + 1)
    if island_x - 1 >= 0 and [island_y, island_x - 1] not in visited and board[island_y][island_x - 1]:
        size_island += 1
        find_count_island(board, island_y, island_x - 1)
    return size_island


# with open("C:\Программирование\ЛабРаб9\start_map.txt", "r") as f:
#     start_map = f.read()


start_map = open("C:\Программирование\ЛабРаб9\start_map.txt", "r")
end_map = open("C:\Программирование\ЛабРаб9\end_map.txt", "w")
board = []
visited = [] # Массив для запоминания координат уже найденного острова
size_island = 0 # Размер 1 острова
count_islands = 0 # Количество островов
k = 0 # Счётчик
general_size_islands = 0 # Количество размеров суши
lines = int(input('Введите размер строк в массиве: '))
columns = int(input('Введите размер столбцов в массиве: '))
size_dragon = int(input('Введите размер дракона: '))
start_size_dragon = size_dragon
start_coordinate = input('Введите стартовую точку для дракона: ')
dragon_y = start_coordinate[0]
dragon_x = int(start_coordinate[1])
count_zero = 1 # Счётчик, обозначающий количество островов после съедения
home = False
if dragon_y == 'W' or dragon_y == 'w':
    dragon_y = int(start_coordinate[1])
    dragon_x = 0
elif dragon_y == 'N' or dragon_y == 'n':
    dragon_y = 0
    dragon_x = int(start_coordinate[1])
elif dragon_y == 'E' or dragon_y == 'e':
    dragon_y = int(start_coordinate[1])
    dragon_x = columns - 1
elif dragon_y == 'S' or dragon_y == 's':
    dragon_y = lines - 1
    dragon_x = int(start_coordinate[1])
for i in range(lines):
    board.append([int(i) for i in start_map.readline().split()])

while count_zero != 0 or home != 1:
    count_zero = 0
    size_island = 0
    island_y, island_x = find_island(dragon_y, dragon_x)
    dragon_y, dragon_x = island_y, island_x    # Перемещение дракона на ближайший остров

    if board[island_y][island_x]:
        size_island += 1
    else:
        break
    find_count_island(board, island_y, island_x)
    if size_island <= size_dragon:
        count_islands += 1
        for x in visited:
            board[x[0]][x[1]] = 0            # Съедаем остров
        general_size_islands += size_island
        size_dragon = start_size_dragon + general_size_islands//5        # Размер дракона
    else:
        home = 1
        break
    visited.clear()
    for i in range(lines):     # Смотрим, остались ли ещё острова
        for j in range(columns):
            if board[i][j] == 1:
                count_zero += 1


if home:
    print('Дом найден!')
    print(f'Координаты дома дракона: [{dragon_y},{dragon_x}]')
else:
    print('Дом не найден')
print(f'Количество съеденных островов: {count_islands}')
print(f'Количество съеденных единиц суши: {general_size_islands}')
print(f'Размер дракона: {size_dragon}')
end_map.write("\n" + "\n" + "Result: ")
for i in range(lines):
    end_map.write("\n" + str(board[i]))