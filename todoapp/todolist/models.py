from django.db import models


class ToDoItem(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title


class Tag(models.Model):
    value = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.value
