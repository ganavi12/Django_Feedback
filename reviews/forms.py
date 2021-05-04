from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name", max_length=50, 
#                 error_messages={"max_length": "please enter shorter name", "required": "ypur name must not be empty"})
#     review_text = forms.CharField(label="Your Review", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ['']

        labels = {
            "username": "Your Name",
            "review_text": "Your Feedback",
            "rating":"Your Rating"
        }

        error_messages = {
            "username": {
                "max_length": "please enter shorter name",
                "required": "ypur name must not be empty"
            }
        }

    