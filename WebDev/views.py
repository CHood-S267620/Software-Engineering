from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *




# home view
def home(response):
    return render(response, 'WebDev/index.html')


def bill_save(response):
    return render(response, 'WebDev/admin_billing.html.html')

def dev_save(response):
    return render(response, 'WebDev/dev_save.html.html')

# admin  dash view
def admin_dash(response):
    return render(response, 'WebDev/admin_dashboard.html')





# Define a view function for the login page
def admin_login(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/admin_login')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/admin_login')
        elif user.is_staff == False:
            # Log in the user and redirect to the home page upon successful login
            messages.error(request, "Admin Privileges Not Found, Redirecting To Login Page")
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/admin_dashboard')
    
    # Render the login page template (GET request)
    return render(request, 'WebDev/admin_login.html')





# view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/client_dashboard')
    
    # Render the login page template (GET request)
    return render(request, 'WebDev/login.html')





# view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register')
        
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
        
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/login')
    
    # Render the registration page template (GET request)
    return render(request, 'WebDev/register.html')




# developer view
def devs(request):
    context ={}
    form = dev_form()
    developers = Developers.objects.all()
    context['developers'] = developers
    if request.method == 'POST':
        # create
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:               
                form = dev_form(request.POST)
            else:
                 dev = Developers.objects.get(DeveloperID=pk)
                 form = dev_form(request.POST, instance=dev)
            form.save()
            form = dev_form()

        # delete
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            dev = Developers.objects.get(DeveloperID=pk)
            dev.delete()

        # Update
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            dev = Developers.objects.get(DeveloperID=pk)
            form = dev_form(instance=dev)

    context['form'] = form

   
    return render(request, 'WebDev/developers.html', context)
        


# website details view
def client_website_details(request):
        context ={}
        context['form']= details_form()
        if request.method=="POST":
            post=details_form(request.POST)
            if post.is_valid():
                post.ClientID=['ClientID']
                post.WebsiteName=['WebsiteName']
                post.WebsiteType=['WebsiteType']
                post.save()
                return redirect('/client_dashboard')
            else:
                post = details_form()
                return redirect('/client_dashboard')
            
        else:
             return render(request, 'WebDev/client_website_details.html', context)



def admin_website_details(request):
    context ={}
    form = details_form()
    details = Website_details.objects.all()
    context['details'] = details
    if request.method == 'POST':
        # create
        if 'web_save' in request.POST:
            pk = request.POST.get('web_save')
            if not pk:               
                form = details_form(request.POST)
            else:
                 ID = Website_details.objects.get(WebsiteID=pk)
                 form = details_form(request.POST, instance=ID)
            form.save()
            form = details_form()

        # delete
        elif 'web_delete' in request.POST:
            pk = request.POST.get('web_delete')
            ID = Website_details.objects.get(WebsiteID=pk)
            ID.delete()

        # Update
        elif 'web_edit' in request.POST:
            pk = request.POST.get('web_edit')
            ID = Website_details.objects.get(WebsiteID=pk)
            form = details_form(instance=ID)

    context['form'] = form

   
    return render(request, 'WebDev/admin_website_details.html', context)


def admin_billing(request):
    context ={}
    form = billing_form()
    bills = Billing.objects.all()
    context['bills'] = bills
    if request.method == 'POST':
        # create
        if 'bill_save' in request.POST:
            pk = request.POST.get('bill_save')
            if not pk:               
                form = billing_form(request.POST)
            else:
                 bill = Billing.objects.get(BillingID=pk)
                 form = billing_form(request.POST, instance=bill)
            form.save()
            form = billing_form()

        # delete
        elif 'bill_delete' in request.POST:
            pk = request.POST.get('bill_delete')
            bill = Billing.objects.get(BillingID=pk)
            bill.delete()

        # Update
        elif 'bill_edit' in request.POST:
            pk = request.POST.get('bill_edit')
            bill = Billing.objects.get(BillingID=pk)
            form = billing_form(instance=bill)

    context['form'] = form

   
    return render(request, 'WebDev/admin_billing.html', context)


# client dash view
@login_required
def client_dash(request):

    # website details
    detail_context ={}
    deatail_form = details_form()
    details = Website_details.objects.filter(ClientID=request.user)
    detail_context['details'] = details
    detail_context['deatail_form'] = deatail_form

    return render(request, 'WebDev/client_dash.html', detail_context)


# client bill view
@login_required
def client_billing(request):

    # website details
    context ={}
    form = billing_form()
    bills = Billing.objects.filter(ClientID=request.user)
    context['bills'] = bills
    #pay
    if 'bill_pay' in request.POST:
        pk = request.POST.get('bill_pay')
        bill = Billing.objects.get(BillingID=pk)
        bill.delete()
    
    context['form'] = form

   
    return render(request, 'WebDev/client_billing.html', context)



