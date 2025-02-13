
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank_u",views.Thank_you_view.as_view()),
    path("reviewList",views.ReviewListView.as_view(),name="reviewList"),
    # path("review/<int:id>",views.Detail_view.as_view(),name="detail")
    path("review/<int:pk>",views.Detail_view.as_view(),name="detail"),
    path("student",views.form_for_table.as_view()),
    path("table",views.Table_create.as_view(),name="student_list"),
    path("table/<int:pk>/update/",views.UpdateStudent.as_view(),name="update"),
    path("table/<int:pk>/delete/",views.DeleteStudent.as_view(),name="delete")
]