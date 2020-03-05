from django.shortcuts import render,redirect
from blog.models import Blogpost
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'home/home.html')
    

def contact(request):
    if (request.method == "POST"):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        txtmsg = request.POST.get('txtmsg', '')
        date1 = datetime.now()
        contact = Contact(name=name, email=email, phone=phone, txtmsg=txtmsg, date=date1)
        contact.save()
        msgDisply = "Thank you Submit Successully!"        
        return render(request, 'home/contact.html', {'msgDisply': msgDisply} )
    else:
        return render(request, 'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def privacy(request):
    return render(request,'home/privacy.html')

def search(request):
    query = request.GET['query']
    if(len(query)>50):
        AllBlogs = Blogpost.objects.none()
    else:
        AllBlogsTitle = Blogpost.objects.filter(title__icontains=query)    
        AllBlogsHeading = Blogpost.objects.filter(heading__icontains=query)  
        AllBlogs = AllBlogsTitle.union(AllBlogsHeading)  
        # AllBlogs = Blogpost.objects.all()
    
    params = {'allpost':AllBlogs,'query':query} 
    return render(request,'home/search.html', params)

def handelSignUp(request):
    if request.method == "POST":
        userName = request.POST['userName']
        fName = request.POST['fName']
        lName = request.POST['lName']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myUser = User.objects.create_user(userName, email, pass1)
        myUser.first_name = fName
        myUser.last_name = lName
        myUser.save()
        return render(request,'home/home.html')
    else:
        return HttpResponse('Not Allowed')  

def handelLogin(request):
     if request.method == "POST":
        loginName = request.POST['loginName']
        loginpassword = request.POST['loginpassword'] 
        user = authenticate(username=loginName, password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect("/home")
        else:
            return HttpResponse("Error!!")
            
     return ("Error 404")   

def handelLogout(request):
    logout(request)
    return redirect("/home")
    return ("Eror 404") 