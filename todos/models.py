from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):

    class TodoState(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        COMPLETED = 'COMPLETED', 'Completed'
        POSTPONED = 'POSTPONED', 'Postponed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    title = models.CharField(max_length=50)
    description = models.TextField()
    due_datetime = models.DateTimeField()
    state = models.CharField(
        max_length=9,
        choices=TodoState.choices,
        default=TodoState.PENDING
    )

    def time_left(self):
        return self.due_datetime - timezone.now()

    def __str__(self):
        return self.title
