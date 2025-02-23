from django.shortcuts import HttpResponse, render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        membership = request.POST.get('membership')
        interest = request.POST.get('interest')

        # Basic validation (You can add more)
        if not email or not password or membership == 'Select membership' or interest == 'Select interest':
            messages.error(request, 'All fields are required.')
            return render(request, 'sign_up.html')

        # Create the user (This is just basic, consider password hashing and more)
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            # Save membership and interest if necessary
            # You can create a model for Membership and Interest
            
            messages.success(request, 'Your account has been created successfully.')
            return redirect('sign_in')  # Redirect to a login page or dashboard
        except Exception as e:
            messages.error(request, f"Error creating user: {str(e)}")
            return render(request, 'sign_up.html')

    return render(request, "sign_up.html")

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')  # Redirect to the user's dashboard or home page
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'sign_in.html')

    return render(request, 'sign_in.html')

