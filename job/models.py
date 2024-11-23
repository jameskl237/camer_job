from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField()
    domain = models.ForeignKey(
        Domain,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    
    def __str__(self):
        return self.title 