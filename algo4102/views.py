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

def index(request):
	xnotiles1 = (9,10,11)
	ynotiles1 = (0,1,2,3,4,5,15,16,17,18,19,20)
	xnotiles2 = ynotiles1
	ynotiles2 = xnotiles1
	context = {('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'index.html',context)

def solve(request):
	if request.method != "POST":
		return "You shouldn't be here yet"
	given = [[0 for x in range(21)] for x in range(21)]
	answer = [[(x%10) for x in range(21)] for x in range(21)]


	for i in request.POST:
		if not i[0]=='c':
			rc = i.split('-')
			given[int(rc[0])][int(rc[1])]=request.POST[i]

	#figure out the answer here
    #the array given should have exactly what was given on the previous screen
    #blank boxes are represented as zeroes
    #the array is a full square. they boxes that shouldn't exist
    #also initialized to zeroes and should stay that way. or not. it shouldn't matter
    #generous amounts of helper methods will likely be needed



	xnotiles1 = (9,10,11)
	ynotiles1 = (0,1,2,3,4,5,15,16,17,18,19,20)
	xnotiles2 = ynotiles1
	ynotiles2 = xnotiles1
	ansstr = two_d_list_to_string(blank_board)
	context = {('ansstr',ansstr),('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'solved.html',context)

def two_d_list_to_string(list):
	ansstr = "test"
	for row in list:
		for col in row:
			if col >= 0:
				ansstr = ansstr + str(col)
			else:
				ansstr = ansstr + "x"
	return ansstr