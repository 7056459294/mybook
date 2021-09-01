from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Contact ,users,books,soldbooks
from math import ceil
from django.contrib import messages 
# Create your views here.
def login(request): 
    if request.method =="POST":
        global email
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        # user data fetch using email
        if  users.objects.filter(email=email).exists():
            userdata=users.objects.filter(email=email)
            userdata=userdata[0]
            userpass=userdata.password
            usertype=userdata.usertype
           
            
            #data_all=signup_user.objects.all()
            if password==userpass:
                if usertype=='Customer':
                    return redirect('/index')
                    #return render(request,'index.html',{"userdata":userdata})
                elif usertype=='Seller':
                    return redirect('/index1')
                    #return render(request,'index1.html',{"userdata":userdata}) 
            else:
                  
                  return redirect('login')
        
    return render(request,'login.html')
        
def signup(request):
    if request.method=="POST":
    
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone_no=request.POST.get('no', '')
        password=request.POST.get('password', '')
        Address=request.POST.get('add', '')
        usertype=request.POST.get('usertype', '')
        print(email)
        print(usertype)
        user = users(name=name, email=email, phone_no=phone_no,Address=Address,usertype=usertype,password=password )
        user.save()
        return redirect('login')
    return render(request, "signup.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "contact.html")

def about(request):
    return render(request, 'about.html')

def index(request):
    allbooks = []
    catbooks = books.objects.values('category','id')
        
    cats = {item['category'] for item in catbooks}
        
    for cat in cats:
       book = books.objects.filter(category=cat)
    
       n = len(book)
    
       nSlides = n // 4 + ceil((n / 4) - (n // 4))
    
       allbooks.append([book, range(1,nSlides),nSlides])
   
       
    
    userdata=users.objects.filter(email=email)
    userdata=userdata[0]
    params = {'allbooks':allbooks}
    return render(request, 'index.html', params)

def index1(request):
    allbooks = []
    catbooks = books.objects.values('category','id')
        
    cats = {item['category'] for item in catbooks}
        
    for cat in cats:
       book = books.objects.filter(category=cat)
    
       n = len(book)
    
       nSlides = n // 4 + ceil((n / 4) - (n // 4))
    
       allbooks.append([book, range(1,nSlides),nSlides])
   
       
    
    userdata=users.objects.filter(email=email)
    userdata=userdata[0]
    params = {'allbooks':allbooks}
    return render(request, 'index1.html', params)
    #return render(request, 'index1.html')
    #return render(request, 'base.html')

def addbooks(request):
    if request.method=="POST":
       book_name=request.POST.get('bookname', '')
       category=request.POST.get('bookcat', '')
       price=request.POST.get('price', '')
       des=request.POST.get('des', '')
       image=request.FILES.get('image')
        
       book = books(book_name=book_name,category=category,price=price,des=des,image=image)
       messages.success(request,'Book Add Successful')
       book.save()
       

    return render(request, 'addbooks.html') 

def deletebooks(request):
    if request.method=="POST":
       book_name=request.POST.get('bookname', '')
       books.objects.filter(book_name=book_name).delete()
       messages.success(request,'Book Delete Successful')
    return render(request, 'deletebooks.html') 

def modifybooks(request):
   if request.method=="POST":
       Mbook_name=request.POST.get('mbookname', '')
       book_name=request.POST.get('bookname', '')
       category=request.POST.get('bookcat', '')
       price=request.POST.get('price', '')
       des=request.POST.get('des', '')
      

       books.objects.filter(book_name=Mbook_name).update(book_name=f"{book_name}")
       books.objects.filter(book_name=Mbook_name).update(category=f"{category}")
       books.objects.filter(book_name=Mbook_name).update(price=f"{price}")
       books.objects.filter(book_name=Mbook_name).update(des=f"{des}")
      
      
       messages.success(request,'Book Modified Successful')
       
   
   return render(request, 'modifybooks.html') 

def soldbook(request):
    bookdata=soldbooks.objects.all()
    bookdatalen=len(bookdata)
   
   
    lendata=[]
    for i in range(1,bookdatalen+1):
        lendata.append(i)
    
    params = {'bookdata':bookdata,'lendata':lendata}
    return render(request,'soldbook.html', params)
    
def buybook(request):
    userdata=users.objects.filter(email=email)
    #bookdata=books.objects.filter(book_name="book1")
    #bookdata=bookdata[0]
    userdata=userdata[0]
    cus_name=userdata.name
    cus_email=userdata.email
    #book_name=bookdata.book_name
    #price=bookdata.price
    book_name="book1"
    price="1000"
    params= {'userdata':userdata}

    solddata=soldbooks(book_name=book_name,cus_name=cus_name,cus_email=cus_email,price=price)
    solddata.save()
    return render(request,'buybook.html',params)
    
