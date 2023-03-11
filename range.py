# range 範圍
# python 內建功能:清單產生器
import random

range(5) # [0, 1, 2, 3, 4]
range(3) #[0, 1, 2]

for i in range(3):
	print('hi')
for i in range(100):
	r = random.randint(1, 1000)
	print('這是第', i + 1, '次產生隨機數', r)

#開頭包含，結尾不包含
#range(開頭值、結尾值、遞增遞減值)
range(2, 5) #[2, 3, 4]
range(8, 10) #[8, 9]
range(2, 10, 3) #[2, 5, 8]
range(3, 8, 2) #[3, 5, 7]
range(10, 3, -2) #[10, 8, 6, 4]
