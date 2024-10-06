from django.db import models
import datetime
# Create your models here.
class note(models.Model):
    NoteID = models.AutoField(primary_key=True)  
    Title = models.CharField(max_length=200)    
    Content = models.TextField()                
    Timestamp = models.DateTimeField()  

    def __str__(self):
        return self.title