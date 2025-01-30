from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name",max_length=100,error_messages={
#         "required": "your name musnt`t be empty",
#         "max_length":"Please enter a shorter name"
#     })
#     review_text = forms.CharField(label="Your feedback",widget=forms.Textarea,max_length=200)
#     rating = forms.IntegerField(label="your rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ='__all__'
        # fields = `[user-name,...]` 
        labels = {
            "user_name" : "your name ",
            "review_text" : "your review",
            "rating" : "your rating"
        }
        error_messages = {
            "user_name":{
                "required" : "your name is required",
                "max_lenght" : "your name must be shorter"
            }
        }