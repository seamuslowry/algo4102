from django.shortcuts import render
from .models import Board

def index(request):
	xnotiles1 = (9,10,11)
	ynotiles1 = (0,1,2,3,4,5,6,15,16,17,18,19,20)
	xnotiles2 = ynotiles1
	ynotiles2 = xnotiles1
	context = {('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'index.html',context)

def solve(request):
	if request.method != "POST":
		return "You shouldn't be here yet"
	xnotiles1 = (9,10,11)
	ynotiles1 = (0,1,2,3,4,5,6,15,16,17,18,19,20)
	xnotiles2 = ynotiles1
	ynotiles2 = xnotiles1
	context = {('lengthRange',xrange(21)),('widthRange',xrange(21)),('xnotiles1',xnotiles1),('ynotiles1',ynotiles1),('xnotiles2',xnotiles2),('ynotiles2',ynotiles2)}
	return render(request, 'solved.html',context)