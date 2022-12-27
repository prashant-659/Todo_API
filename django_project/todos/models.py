from django.db import models

#The body and title of the Todo_API is defined here
class Todo(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()

    def __str__(self):
        return self.title