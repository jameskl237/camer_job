from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='no_email@mail.com')
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', default='no_image')
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='users'  
    )

    def __str__(self):
        return self.name
    