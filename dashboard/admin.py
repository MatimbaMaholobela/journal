from django.contrib import admin

from .models import JournalEntry

# Register your models here.
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('date','title','journal_entry')
 
 
 
admin.site.register(JournalEntry, JournalEntryAdmin)
