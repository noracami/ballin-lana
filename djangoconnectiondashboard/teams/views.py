from django.shortcuts import render

# Create your views here.
def team_list(request):
    return render(request, 'teams/team_list.html', {})

def team_detail(request):
    return render(request, 'teams/team_detail.html', {})
