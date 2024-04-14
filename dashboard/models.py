from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    date=models.DateTimeField(blank=False)
    title=models.TextField(blank=False,max_length = 100)
    journal_entry= models.TextField(blank=True,max_length = 120)
    
