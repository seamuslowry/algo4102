from django.db import models

class Board(models.Model):
	length = models.PositiveIntegerField()
	width = models.PositiveIntegerField()
	array = [[]]

class Problem(models.Model):
	board = models.ForeignKey(Board)

class Piece(models.Model):
	problem = models.ForeignKey(Problem)
	array = [[]]