from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import Contact, Blogpost

# Register your models here.
class ContactAdmin(ModelAdmin):
    list_display = ["name","email","date"]
    search_fields =["name"]
    list_filter = ["date"]

class BlogpostAdmin(ModelAdmin):
     list_display = ["title","heading","pub_date"]
     search_fields = ["title"]
     list_filter = ["pub_date"]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Blogpost, BlogpostAdmin)