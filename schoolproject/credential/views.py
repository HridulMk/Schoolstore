from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'NewPage.html')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if not username or not first_name or not last_name or not email or not password or not cpassword:
            messages.error(request, "All fields are required")
            return redirect('register')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();
                return redirect('login')
            messages.info(request,"user created")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def newregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials_provide = request.POST.getlist('materials_provide')
        if not username or not phone or not email:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('newregister')
        if len(phone) != 10:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
                return redirect('newregister')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken.')
                return redirect('newregister')
            elif User.objects.filter(profile__phone=phone).exists():
                messages.error(request, 'Phone already taken.')
                return redirect('newregister')
            else:
                 register=User.objects.create_register(username=username,email=email,phone=phone,dob=dob,age=age,gender=gender,address=address,department=department,course=course,purpose=purpose,materials_provide=materials_provide)
                 register.save();
                 messages.info(request, 'Order Successfully Submited.')
                 return redirect('newregister')

        else:
            messages.error(request, 'Order Successfully Submited.')
            return redirect('newregister')

        # Add your logic to process the form data or save it to the database

               # Redirect to the same page after submission

    return render(request,'newregister.html')

