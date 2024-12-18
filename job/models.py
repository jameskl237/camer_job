from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Domain(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    class TaskStatus(models.TextChoices):
        FREE = 'FR', _('Free')
        DURING = 'D', _('During')
        FINISH = 'FN', _('Finish')
        
    title = models.CharField(max_length=255)
    description = models.TextField()
    Price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.FREE)
    created_at = models.DateTimeField(default=timezone.now)
    domain = models.ForeignKey(
        Domain,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    # def __str__(self):
    #     return self.title 