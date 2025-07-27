from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, Http404
import os

# 🔐 Service Provider Login View
def serviceproviderlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "admin" and password == "admin":
            request.session['username'] = username
            return redirect('serviceprovider_home')  # Make sure this URL/view exists
        else:
            return render(request, 'serviceproviderlogin.html', {'error': "Invalid Credentials"})
    return render(request, 'serviceproviderlogin.html')

# ✅ Sample Home View (Add this if not already present)
def serviceprovider_home(request):
    if 'username' in request.session:
        return render(request, 'serviceprovider_home.html')
    else:
        return redirect('serviceproviderlogin')


# ✅ Other Views
def View_Remote_Users(request):
    return render(request, 'View_Remote_Users.html')

def charts(request, chart_type):
    return render(request, 'charts.html', {'chart_type': chart_type})

def charts1(request, chart_type):
    return render(request, 'charts1.html', {'chart_type': chart_type})

def likeschart(request, like_chart):
    return render(request, 'likeschart.html', {'like_chart': like_chart})

def Find_Predict_Jop_Post_Type_Details_Ratio(request):
    return render(request, 'Find_Predict_Jop_Post_Type_Details_Ratio.html')

def Predict_Jop_Post_Type_Details(request):
    return render(request, 'Predict_Jop_Post_Type_Details.html')

def train_model(request):
    return render(request, 'train_model.html')

from django.shortcuts import redirect

def logout_view(request):
    request.session.flush()  # clears all session data
    return redirect('serviceproviderlogin')  # redirect to login page
from django.shortcuts import render, redirect
from django.contrib import messages

def serviceproviderlogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        # Simple static login (replace with DB-based logic later)
        if uname == "admin" and pwd == "admin":
            request.session['username'] = uname
            return redirect('serviceprovider_home')  # ensure this route exists in urls.py
        else:
            messages.error(request, 'Invalid Login Credentials')
            return render(request, 'serviceproviderlogin.html')

    return render(request, 'serviceproviderlogin.html')
def serviceprovider_home(request):
    return render(request, 'serviceprovider_home.html')



def Download_Trained_DataSets(request):
    filepath = os.path.join("your_app", "trained_dataset.csv")  # Change to actual file path
    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), as_attachment=True)
    else:
        raise Http404("File does not exist.")
