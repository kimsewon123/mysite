from django.contrib import admin
from .models import Board,Comment

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    
admin.site.register(Board, BoardAdmin)
admin.site.register(Comment)