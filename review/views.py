from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm , TableForm
from .models import Review,Student
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView, CreateView
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name= "review/review.html"
    success_url = "/thank_u"

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "review/review.html"
#     success_url = "/thank_u"
#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)

        
# class ReviewView(View):

#     def get(self,request):
#         form = ReviewForm()
#         return render (request,"review/review.html",{"form":form})
#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # view =Review(
#             #     user_name = form.cleaned_data['user_name'],
#             #     review_text = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating']
#             # )
#             # view.save()
#             form.save()
#             return HttpResponseRedirect("/thank_u")




def review(request):
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # view =Review(
            #     user_name = form.cleaned_data['user_name'],
            #     review_text = form.cleaned_data['review_text'],
            #     rating = form.cleaned_data['rating']
            # )
            # view.save()
            form.save()
            return HttpResponseRedirect("/thank_u") 
    else:
        form = ReviewForm()


    # enviamoslle o formulario a planilla review
    # se o usuario envio datos ese form vai ter os datos
    # si se carga la pagina por primera vez este se cargara vacio
    return render(request,"review/review.html",{"form":form})

def thank_u(request):
    return render(request,"review/thank_u.html")

class Thank_you_view(TemplateView):
    template_name = "review/thank_u.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    
# class ReviewListView(TemplateView):
#     template_name = "review/review_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
    
class ReviewListView(ListView):
    template_name  = "review/review_list.html"
    model = Review
    context_object_name = "reviews"



# class Detail_view(TemplateView):
#     template_name = 'review/details.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id= kwargs["id"]
#         element = Review.objects.get(pk=review_id)
#         context["element"]=element
#         return context

class Detail_view(DetailView):
    template_name = "review/details.html"
    model = Review
    context_object_name = "element"


# table

class form_for_table(CreateView):
    model = Student
    form_class = TableForm
    template_name= "table/index.html"
    success_url = "/table"

class Table_create(ListView):
    template_name  = "table/table.html"
    model = Student
    context_object_name = "students"

class UpdateStudent(UpdateView):
    model = Student
    form_class = TableForm
    template_name= "table/index.html"
    success_url = "/table/"

class DeleteStudent(DeleteView):
    model = Student
    form_class = TableForm
    template_name = "table/confirm_delete.html"
    success_url = "/table/"