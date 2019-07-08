print("Hello Universe!!!")
'''
prog_lang = ("py", "c++")
vehicles = ["car","bike","Cycle"]
l = [1,2,3,4,5,6,7,8] 
print(l[2:])
print(type(prog_lang))
for language in prog_lang:
	print(language)
'''
'''game = [[0,0,0],
		[0,0,0],
		[0,0,0],]

def game_board(game_map, player=0, row=0, column=0):
	try:
		print("   a  b  c")
		game_map[row][column]=33
		for count, row in enumerate(game_map):
			print(count  , row)
		return game_map
	except IndexError as e: 
		print("Error: Index should be 0 to 2", e)
	except Exception as e: 
		print("Something went Very wrong", e)

game = game_board(game)
game = game_board(game_board,player=1,row=0,column=1)
 
game[0][1] = 1
x = game_board
x()
items = ['tomato','banana', 'Orange']
print(list(enumerate((items))))

print('ENU')
for i in enumerate([2,6,8,9],start = 34):
	print(i)

x = [0,1,2,3,4,5,6]
y = [4,3,2,1,0,9]
z = [1,5,8,2]

for i in zip(x,y,z):
	print(i) 
'''
game = [[2,1,1],
		[2,2,0],
		[1,1,2]]

def winner(game):

	# row winner 
	for row in game:
		if (row.count(row[0]) == len(row) and row[0] != 0):
			print(f"Player {row[0]} is the Winner horizontally!")

	# column winner 
	for col in range(len(game)):
		check = []
		for row in game:
			check.append(row[col])
		if (check.count(check[0]) == len(check) and check[0] != 0):
			print(f"Player {check[0]} is the Winner vertically!")

	# "/" diagonal 
	diag = []
	for col, row in enumerate(reversed(range(len(game)))): 
		diag.append(game[col][row]) 
	if diag.count(diag[0]) == len(diag) and diag[0] != 0:
		print(f"Player {diag[0]} is the Winner diagonally!")
	
	# "\" diagonal 
	diag = [] 
	for i in range(len(game)):
		diag.append(game[i][i])
	if diag.count(diag[0]) == len(diag) and diag[0] != 0:
		print(f"Player {diag[0]} is the Winner diagonally!")

winner(game)
