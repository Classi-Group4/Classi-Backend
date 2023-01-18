from django.db import models
from django.contrib.auth import get_user_model

class Classes(models.Model) : 
    class_name = models.CharField(max_length=255)
    description =models.CharField(max_length=255)    
    category =models.CharField(max_length=255)
    available_time = models.CharField(max_length= 255)
    location = models.CharField(max_length=255)
    price =models.IntegerField()
    teacher_name = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)


    def __str__(self):
        return self.class_name
