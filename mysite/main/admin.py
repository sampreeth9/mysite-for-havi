from django.contrib import admin
from .models import Country , State , District , Mandal , Location , User_table

# Register your models here.
modelList = [Country,State,District,Mandal,Location,User_table]
admin.site.register(modelList)
