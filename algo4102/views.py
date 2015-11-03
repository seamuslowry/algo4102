from django.shortcuts import render
from .models import Board

blank_board = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
			   [-1,-1,-1,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1,-1,-1,-1],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [ 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,-1,-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

xnotiles1 = (9,10,11)
ynotiles1 = (0,1,2,3,4,5,15,16,17,18,19,20)
xnotiles2 = ynotiles1
ynotiles2 = xnotiles1

TOP_LEFT = 0
TOP_RIGHT = 1
MIDDLE = 2
BOT_LEFT = 3
BOT_RIGHT = 4
NONE = -1

def index(request):
	context = {('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'index.html',context)

def solve(request):
	if request.method != "POST":
		return "You shouldn't be here yet"
	given = blank_board
	answer = [[(x%10) for x in range(21)] for x in range(21)]


	for i in request.POST:
		if not i[0]=='c':
			rc = i.split('-')
			if (request.POST[i]):
				given[int(rc[0])][int(rc[1])]=request.POST[i]
			else:
				given[int(rc[0])][int(rc[1])]=0


	#figure out the answer here
	#the array given should have exactly what was given on the previous screen
	#blank boxes are represented as zeroes
	#the array is a full square. they boxes that shouldn't exist
	#also initialized to zeroes and should stay that way. or not. it shouldn't matter
	#generous amounts of helper methods will likely be needed

	#please do not modiy below here in this method either
	#everything is held together by spit and prayers

	ansstr = two_d_list_to_string(given)
	context = {('ansstr',ansstr),('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'solved.html',context)

def two_d_list_to_string(list):
	ansstr = "test"
	for row in list:
		for col in row:
			if col >= 0:
				ansstr = ansstr + str(col)
			elif col == 0:
				ansstr = ansstr + "z"
			else:
				ansstr = ansstr + "x"
	return ansstr

def is_valid(r,c):
	# print "c: " + str(c) + "in xnotiles1: " + str(c in xnotiles1)
	# print "c: " + str(c) + "in xnotiles2: " + str(c in xnotiles2)
	# print "r: " + str(r) + "in ynotiles1: " + str(r in xnotiles1)
	# print "r: " + str(r) + "in ynotiles2: " + str(r in xnotiles2)
	return not (c in xnotiles1 and r in ynotiles1 or c in xnotiles2 and r in ynotiles2)

def determine_boards_or_invalid(r,c):
	if not is_valid(r,c):
		return [NONE]
	ret = []
	if c < 9 and r < 9:
		ret.append(TOP_LEFT)
	if c > 11 and r < 9:
		ret.append(TOP_RIGHT)
	if c > 11 and r > 11:
		ret.append(BOT_RIGHT)
	if c < 9 and r > 11:
		ret.append(BOT_LEFT) 
	if c > 5 and c < 15 and r > 5 and r < 15:
		ret.append(MIDDLE)
	return ret

#given the larger 21x21 board in large_board
#determine whether inserting val at r,c is a valid move

def check_board(large_board,r,c,val):
	#for this, remember that python is pass-by-value
	boards = determine_boards_or_invalid(r,c)
	if -1 in boards:
		return False
	for b_index in boards:
		b = get_board(large_board,b_index)
		validate(b) # just returns true right now

def get_board(board,b_index):
	if b_index==TOP_LEFT:
		return get_top_left(board)
	elif b_index==TOP_RIGHT:
		return get_top_right(board)
	elif b_index==BOT_LEFT:
		return get_bot_left(board)
	elif b_index==BOT_RIGHT:
		return get_bot_right(board)
	elif b_index==MIDDLE:
		return get_middle(board)
	else:
		return null;

def get_top_left(board): 
	ret = [[c for c in r[:9]] for r in board[:9]]
	return ret

def get_top_right(board): 
	ret = [[c for c in r[12:]] for r in board[:9]]
	return ret

def get_bot_right(board): 
	ret = [[c for c in r[12:]] for r in board[12:]]
	return ret

def get_bot_left(board): 
	ret = [[c for c in r[:9]] for r in board[12:]]
	return ret

def get_middle(board):
	ret = [[c for c in r[6:15]] for r in board[6:15]]
	return ret

def validate(board):
	return True