from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pictures')
    desc1=models.TextField()

    def __str__(self):
        return self.name1