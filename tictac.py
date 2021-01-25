import time
import random as r
def makeboard(board):
        print(board[0],'|',board[1],'|',board[2])
        print('--+---+--')
        print(board[3],'|',board[4],'|',board[5])
        print('--+---+--')
        print(board[6],'|',board[7],'|',board[8])



def winning_checker(board,tom,user):
	row1 = [board[0],board[1],board[2]]
	row2 = [board[3],board[4],board[5]]
	row3 = [board[6],board[7],board[8]]
	col1 = [board[0],board[3],board[6]]
	col2 = [board[1],board[4],board[7]]
	col3 = [board[2],board[5],board[8]]
	dia1 = [board[0],board[4],board[8]]
	dia2 = [board[2],board[4],board[6]]
	for row in [row1,row2,row3,col1,col2,col3,dia1,dia2]:
		if row == [user,user,user]:
			return 'you win'
			break
		if row == [tom,tom,tom]:
			return 'computer wins'
			break

def AI_simulator(board,tom,user,u):
	row1 = [board[0],board[1],board[2]]
	row2 = [board[3],board[4],board[5]]
	row3 = [board[6],board[7],board[8]]
	col1 = [board[0],board[3],board[6]]
	col2 = [board[1],board[4],board[7]]
	col3 = [board[2],board[5],board[8]]
	dia1 = [board[0],board[4],board[8]]
	dia2 = [board[2],board[4],board[6]]
	tabs = [row1,row2,row3,col1,col2,col3,dia1,dia2]
	for row in tabs:
		if row == [' ',tom,tom]:
			x = tabs.index(row)
			if x == 0:
				board[0] = tom
			if x == 1:
				board[3] = tom
			if x == 2:
				board[6] = tom
			if x == 3:
				board[0] = tom
			if x == 4:
				board[1] = tom
			if x == 5:
				board[2] = tom
			if x == 6:
				board[0] = tom
			if x == 7:
				board[2] = tom
			print('tom played:')
			makeboard(board)
			break
		elif row == [tom,' ',tom]:
			x = tabs.index(row)
			if x == 0:
				board[1] = tom
			if x == 1:
				board[4] = tom
			if x == 2:
				board[7] = tom
			if x == 3:
				board[3] = tom
			if x == 4:
				board[4] = tom
			if x == 5:
				board[5] = tom
			if x == 6:
				board[4] = tom
			if x == 7:
				board[4] = tom
			print('tom played:')
			makeboard(board)
			break
		elif row == [tom,tom,' ']:
			x = tabs.index(row)
			if x == 0:
				board[2] = tom
			if x == 1:
				board[5] = tom
			if x == 2:
				board[8] = tom
			if x == 3:
				board[6] = tom
			if x == 4:
				board[7] = tom
			if x == 5:
				board[8] = tom
			if x == 6:
				board[8] = tom
			if x == 7:
				board[6] = tom
			print('tom played:')
			makeboard(board)
			break
	if (row != [' ',tom,tom] and row != [tom,' ',tom] and row != [tom,tom,' ']):
		time.sleep(1)
		AI_block(board,tom,user)

def AI_block(board,tom,user):
	row1 = [board[0],board[1],board[2]]
	row2 = [board[3],board[4],board[5]]
	row3 = [board[6],board[7],board[8]]
	col1 = [board[0],board[3],board[6]]
	col2 = [board[1],board[4],board[7]]
	col3 = [board[2],board[5],board[8]]
	dia1 = [board[0],board[4],board[8]]
	dia2 = [board[2],board[4],board[6]]
	tabs = [row1,row2,row3,col1,col2,col3,dia1,dia2]
	for row in tabs:
		if row == [' ',user,user]:
			x = tabs.index(row)
			if x == 0:
				board[0] = tom
			if x == 1:
				board[3] = tom
			if x == 2:
				board[6] = tom
			if x == 3:
				board[0] = tom
			if x == 4:
				board[1] = tom
			if x == 5:
				board[2] = tom
			if x == 6:
				board[0] = tom
			if x == 7:
				board[2] = tom
			print('tom played:')
			makeboard(board)
			break
		elif row == [user,' ',user]:
			x = tabs.index(row)
			if x == 0:
				board[1] = tom
			if x == 1:
				board[4] = tom
			if x == 2:
				board[7] = tom
			if x == 3:
				board[3] = tom
			if x == 4:
				board[4] = tom
			if x == 5:
				board[5] = tom
			if x == 6:
				board[4] = tom
			if x == 7:
				board[4] = tom
			print('tom played:')
			makeboard(board)
			break
		elif row == [user,user,' ']:
			x = tabs.index(row)
			if x == 0:
				board[2] = tom
			if x == 1:
				board[5] = tom
			if x == 2:
				board[8] = tom
			if x == 3:
				board[6] = tom
			if x == 4:
				board[7] = tom
			if x == 5:
				board[8] = tom
			if x == 6:
				board[8] = tom
			if x == 7:
				board[6] = tom
			print('tom played:')
			makeboard(board)
			break
	if (row != [' ',user,user] and row != [user,' ',user] and row != [user,user,' ']):
		AI_decisionbox(board,tom,user)

def AI_decisionbox(board,tom,user):
	count = 0
	for posn in range(9):
		if board[posn] == ' ':
			board[posn] = user
			row1 = [board[0],board[1],board[2]]
			row2 = [board[3],board[4],board[5]]
			row3 = [board[6],board[7],board[8]]
			col1 = [board[0],board[3],board[6]]
			col2 = [board[1],board[4],board[7]]
			col3 = [board[2],board[5],board[8]]
			dia1 = [board[0],board[4],board[8]]
			dia2 = [board[2],board[4],board[6]]
			tabs = [row1,row2,row3,col1,col2,col3,dia1,dia2]
			for row in tabs:
				if (row == [' ',user,user]) or (row == [user,' ',user]) or (row == [user,user,' ']):
					count += 1
			if count >= 2:
				board[posn] = tom
				print('tom played:')
				makeboard(board)
				break
			else:
				board[posn] = ' '
				count = 0
	if count < 2:
		while True:
				n = r.choice([0,2,6,8])
				if board[n] == ' ':
					board[n] = tom
					print('tom played: ')
					makeboard(board)
					break
				else:
					nu = r.randint(0,8)
					if board[nu] == ' ':
						board[nu] = tom
						print('tom played: ')
						makeboard(board)
						break
while True:				
	entry = input('choose between O and X: ')
	user = entry.upper()
	while user not in ['X','O','x','o']:
		print('X and O are the recommended markers')
		entry = input()
		user = entry.upper()
	if (user == 'X') or (user == 'x'):
		tom = 'O'
	else:
		tom = 'X'
	board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	k = 0
	u = 0
	t = 0
	corners = [0,2,6,8]
	while True:
		if k == 0:
			makeboard(board)
		num = int(input('choose a number between 0 and 8: '))
		while True:
			if num > 8:
				print('number must be from 1 to 8')
				num = int(input('enter number again'))
			break
		while True:
			if board[num] != ' ':
				print('this number has been chosen please choose another')
				num =int(input())
			else:
				board[num] = user
				print('you played:')
				makeboard(board)
				break
		if u >= 2:
			winning_checker(board,tom,user)
			if winning_checker(board,tom,user) == 'you win':
				time.sleep(1)
				print('you win')
				break
		u += 1
		if k == 4:
			print('the game ends in a draw')
			break
		print('its tom turn')
		time.sleep(1)
		if t == 0:
			while True:
				if board[4] == ' ':
					board[4] = tom
					print('tom played:')
					makeboard(board)
					break
				elif board[4] != ' ':
					p = r.choice(corners)
					if board[p] == ' ':
						board[p] = tom
						print('tom played:')
						makeboard(board)
						break
				#else:
				#	nu = r.randint(0,8)
				#	if board[nu] == ' ':
				#		board[nu] = tom
				#		print('tom played: ')
				#		makeboard(board)
				#		break
		if t > 0:
			if t == 1:
				if (board[0] == user and board[8] == user) or (board[2] == user and board[6] == user):
					while True:
						q = r.choice([1,3,5,7])
						if board[q] == ' ':
							board[q] = tom
							print('tom played:')
							makeboard(board)
							break
				else:
					AI_simulator(board,tom,user,u)
					winning_checker(board,tom,user)
			else:
				AI_simulator(board,tom,user,u)
				winning_checker(board,tom,user)
		if winning_checker(board,tom,user) == 'computer wins':
			print('tom wins')
			break
		t += 1
		k += 1
		time.sleep(1)
	print('Do you want to play again')
	time.sleep(1)
	reply = input('enter yes to play again: ')
	reply = reply.lower()
	if reply == 'yes':
		continue
	else:
		time.sleep(1)
		print('thank you for playing')
		break