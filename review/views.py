from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# Create your views here.
def review(request):
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            view =Review(
                user_name = form.cleaned_data['user_name'],
                review_text = form.cleaned_data['review_text'],
                rating = form.cleaned_data['rating']
            )
            view.save()
            return HttpResponseRedirect("/thank_u")
    else:
        form = ReviewForm()


    # enviamoslle o formulario a planilla review
    # se o usuario envio datos ese form vai ter os datos
    # si se carga la pagina por primera vez este se cargara vacio
    return render(request,"review/review.html",{"form":form})

def thank_u(request):
    return render(request,"review/thank_u.html")