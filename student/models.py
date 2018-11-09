from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class StudentInfo(models.Model):
    name = models.CharField(max_length=30)
    father = models.CharField(max_length=30)
    gpa = models.CharField(max_length=30)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    roll = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    
