from django.urls import path


from .views import JobListCreateAPI,JobDetailUpdateDeleteAPI


urlpatterns = [
    path('',JobListCreateAPI.as_view()),
    path('<int:pk>',JobDetailUpdateDeleteAPI.as_view())
]





