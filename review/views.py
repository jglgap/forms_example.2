from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def review(request):
    if request.method=='POST':
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/thank_u")
    return render(request,"review/review.html")
def thank_u(request):
    return render(request,"review/thank_u.html")