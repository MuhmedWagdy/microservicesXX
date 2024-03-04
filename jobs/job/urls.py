from django.urls import path


from .views import JobListCreateAPI,JobDetailUpdateDeleteAPI


urlpatterns = [
    path('',JobListCreateAPI.as_view()),
    path('<slug:slug>',JobDetailUpdateDeleteAPI.as_view())
]





