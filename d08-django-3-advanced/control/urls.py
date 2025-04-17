from django.urls import path
from control.views import ArticlesView

urlpatterns = [
    path('', ArticlesView.as_view()),
]
