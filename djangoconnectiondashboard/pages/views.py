from django.shortcuts import render, redirect

# Create your views here.
def home(requset):
    return redirect('team_list')
    return render(requset, 'pages/home.html', {})
