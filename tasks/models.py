from django.db import models

CATEGORY_CHOICES = [
    ('work', 'Work'),
    ('personal', 'Personal'),
    ('study', 'Study'),
    ('other', 'Other')
]

PRIORITY_CHOICES = [
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High')
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    deadline = models.DateField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    status = models.BooleanField(default=False)  # False = Pending, True = Completed

    def __str__(self):
        return self.title
