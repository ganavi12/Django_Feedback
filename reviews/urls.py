from django.urls import path
from . import views

urlpatterns = [  
    # path("", views.review),
    path("",views.ReviewView.as_view()),
    # path("thankyou",views.thank_you)
    path("thankyou", views.ThankYouView.as_view()),
    path("review", views.ReviewListView.as_view()),
    path("review/<int:pk>",views.SingleReviewView.as_view()),
]