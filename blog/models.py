from django.db import models

# Create your models here.
#Contact Us Table Here
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70, default="")
    txtmsg = models.TextField(default="")
    date = models.DateField(auto_now_add=True)

  

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,default="")
    heading = models.TextField(default="")
    text_details = models.TextField(default="")
    author = models.CharField(max_length=50,default="")      
    slug = models.CharField(max_length=100,default="")      
    pub_date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="blog/images", default="")


