from django.shortcuts import render

# Create your views here.
def create_user_page(request):
    return render(request,"../templates/user/create_user_page.html")

def user_page(request):
    return render(request,"../templates/user/user_page.html")