from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

# Create your views here.

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST) 
        if form.is_valid(): 
            review = Review(username=form.cleaned_data['username'],review_text =form.cleaned_data['review_text'],rating =form.cleaned_data['rating'] )
            review.save()
            # print(form.cleaned_data)
            # entered_username = request.POST['username']
        # if entered_username == "" or not entered_username.isalpha(): 
        #     return render (request,"reviews/review.html",{"has_error" : True})
        # print("response is",entered_username)
            return HttpResponseRedirect("/thankyou")
    form = ReviewForm()
    return render(request, "reviews/review.html", {"form": form})
    
    
def thank_you(request):
    return render(request,'reviews/thank_you.html')