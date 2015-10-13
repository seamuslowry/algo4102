from django.shortcuts import render
from .models import Board

def index(request):
	Board.objects.all().delete()
	return render(request, 'index.html')

def generateBoard(request, pieces):
	if (request.method=="POST"):
		p = Board(length=request.POST['length'],width=request.POST['width'])
		p.save()
	else:
		p = Board.objects.all()[0]
	context = {('lengthRange',xrange(int(p.length))),('widthRange',xrange(int(p.width))),('piecesRange',xrange(1,int(pieces)+1)),('pieces',int(pieces)+1)}
	return render(request, 'generateBoard.html',context)

def createProblem(request, pieces):
	return render(request, 'index.html')