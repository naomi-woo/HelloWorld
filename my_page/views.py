from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(
        request, 
        'my_page/mypage.html'
    )

def profile(request):
    return render(
        request,
        'my_page/profile.html'
    )
    