from django.urls import path
from . import views

urlpatterns = [  
    # path("", views.review),
    path("",views.ReviewView.as_view()),
    path("thankyou",views.thank_you) 
]