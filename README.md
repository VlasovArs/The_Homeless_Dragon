# The_Homeless_Dragon
English language:
Additional task in computer science: "Homeless Dragon"
is given an arbitrary two-dimensional array. In the array, some conventional symbol indicates land areas. The land plots connected vertically or horizontally are islands. The land plots connected diagonally are separate islands. This is our map. The method of setting the array is not essential.
Example:
1 1 0 0 0 0 0 1
0 1 0 0 0 0 1 0
0 0 1 1 0 0 0 0
0 0 1 1 0 0 0 0
0 0 0 0 0 0 1 1
1 1 1 0 0 0 1 1
0 0 1 0 0 0 1 1

Two diagonally connected land plots in the upper right corner are two different islands.
A dragon comes to our islands in search of a home. The dragon has 2 characteristics:
The size of our dragon and the point where it comes from.
The size of the dragon is an integer, denotes the number of land plots that the dragon is able to swallow at a time.
Arrival point is a string in the format: [N/S/E/W] + number. The first letter is the designation of the side from which the dragon arrives. N – north, S – south, W – west, N – east. Next comes a number that denotes the index of the cell from which the dragon arrives. In the example below, coordinates are written in some cells. The coordinates of the corners can be denoted in two ways. In the example, the lower-left corner can be designated as W7 or as S0.
The method of setting the characteristics is not essential.

Example:
1 1 0 N3 0 0 0 1
0 1 0 0 0 0 1 0 0
W2 0 1 1 0 0 0 0
0 0 1 1 0 0 0 E3
0 0 0 0 0 0 1 1
1 1 1 0 0 0 1 1
0 0 1 0 0 0 1 1
W7/S0 0 0 0 0 S5 0 0 0

After the dragon appeared on our lands, he immediately begins to look for a home. To do this, he flies to the nearest piece of land from him. The distance between the cells should be calculated in such a way that the indexes of the cells are their coordinates on the plane. If the size of the dragon is greater than or equal to the size of the island to which it has flown, the dragon cannot make its home on it. This makes him so annoyed that he eats the whole island. The island disappears from the map.
For every 5 units of sushi eaten, the dragon increases its size by 1. After that, the dragon flies further to the nearest piece of land. If the size of the island to which the dragon flew is larger than its size, then it remains there to live and the program terminates on this.
Calculations take place until the dragon finds a home, or until it eats all the land on the map.
NOTE: Despite its size, the dragon always occupies only one square on the map, because it is magical.
After the program is completed, the following characteristics should be output:
Final map
The number of islands that the dragon ate
The number of units of sushi that the dragon ate
Has the dragon found a home for itself
The coordinate of the house (if found)
Requirements for writing a program:
All variables must have a meaningful name.
The code should have comments to improve perception.
It requires 100% understanding of your own code, it's enough to write it yourself.
The code must be unique. This is not a group task, you can exchange the principles of implementation, but if I see two codes that are too similar to each other, both students will be deprived of the automaton.

Russian language:

Дополнительное задание по информатике: «Бездомный дракон»
Дан произвольный двумерный массив. В массиве некоторым условным символом обозначены участки суши. Участки суши, соединенные по вертикали или горизонтали, являются островами. Участки суши, соединенные по диагонали, являются отдельными островами. Это наша карта. Метод задания массива не существенен.
Пример:
1	1	0	0	0	0 0	1
0 1	0	0	0	0	1	0
0	0	1	1	0	0	0	0
0	0	1	1	0	0	0	0
0	0	0	0	0	0	1	1
1	1	1	0	0	0	1	1
0	0	1	0	0	0	1	1
							
Два соединённых по диагонали участка суши в правом верхнем углу – два разных острова.
На наши острова в поисках дома прилетает дракон. У дракона есть 2 характеристики:
Размер нашего дракона и точка откуда он прилетает.
Размер дракона – целое число, обозначает количество участков суши, которое дракон способен проглотить за один раз.
Точка прилёта – строка в формате: [N/S/E/W] + число. Первая буква – обозначение стороны, с которой прилетает дракон. N – север, S – юг, W – запад, N – восток. Далее идёт число, которое обозначает индекс, клетки, с которой прилетает дракон. В примере ниже в некоторых ячейках написаны координаты. Координаты углов могут обозначаться двумя способами. В примере левый нижний угол может быть обозначен, как W7 или как S0.
Способ задания характеристик не существенен.
 
Пример:
1	1	0	N3	0	0	0	1
0	1	0	0	0	0	1	0 0
W2	0	1	1	0	0	0	0
0	0	1	1	0	0 0	E3
0	0	0	0	0	0	1	1
1	1	1	0	0	0	1	1
0	0	1	0	0	0	1	1
W7/S0	0	0	0	0	S5 0 0 0

После того, как дракон появился на наших землях, он немедленно начинает искать себе дом. Для этого он летит к ближайшему от него участку суши. Расстояние между ячейками следует рассчитывать таким образом, будто индексы ячеек являются их координатами на плоскости. Если размер дракона больше или равен размеру острова, к которому он подлетел, дракон не может устроить на нём свой дом. От этого он так раздосадован, что съедает весь остров. Остров с карты пропадает. 
За каждые 5 съеденных единиц суши, дракон увеличивает свой размер на 1. После этого, дракон летит дальше к ближайшему участку суши. Если размер острова, к которому подлетел дракон больше его размера, то он остаётся там жить и на этом программа завершает работу.
 Вычисления происходят до тех пор, пока дракон не найдёт себе дом, либо пока не съест всю сушу на карте.
ПРИМЕЧАНИЕ: несмотря на свой размер, дракон всегда занимает на карте всего одну клетку, потому что он волшебный.
После завершения программы должны быть выведены следующие характеристики:
Итоговая карта
Количество островов, которые съел дракон
Количество единиц суши, которое съел дракон
Нашёл ли дракон себе дом
Координата дома (если нашёл)
Требования к написанию программы:
Все переменные должны иметь осмысленное название.
Код должен иметь комментарии для улучшения восприятия.
Требуется 100% понимание собственного кода, для этого достаточно написать его самому.
Код должен быть уникальным. Это не групповое задание, можете обмениваться принципами реализации, но, если я увижу два слишком похожих друг на друга кода, автомата будут лишены оба студента.
