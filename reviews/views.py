from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponseNotFound
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form": form})
    
#     def post(self, request):
#         form = ReviewForm(request.POST) 
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thankyou")
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form": form})


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thankyou"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thankyou"


    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {"form": form})
    
    # def post(self, request):
    #     form = ReviewForm(request.POST) 
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thankyou")
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {"form": form})

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST) 
        if form.is_valid():
            form.save()
            # review = Review(username=form.cleaned_data['username'],review_text =form.cleaned_data['review_text'],rating =form.cleaned_data['rating'] )
            # review.save()
            # print(form.cleaned_data)
            # entered_username = request.POST['username']
        # if entered_username == "" or not entered_username.isalpha(): 
        #     return render (request,"reviews/review.html",{"has_error" : True})
        # print("response is",entered_username)
            return HttpResponseRedirect("/thankyou")
    form = ReviewForm()
    return render(request, "reviews/review.html", {"form": form})
    
    
def thank_you(request):
    return render(request, 'reviews/thank_you.html')
    

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "this works"
        return context
    
    # def get(self, request):
    #     return render(request, 'reviews/thank_you.html')


# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context



class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data
    
   

# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context         



class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    