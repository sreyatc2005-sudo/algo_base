"""
URL configuration for code_wise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from repository.views import QuestionsListCreateView
from repository.views import QuestionRetrieveUpdateDeleteView
from repository.views import SubmissionListCreateView
from repository.views import SubmissionRetrieveUpdateDeleteView
from repository.views import EvaluateSubmissionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("questions/",QuestionsListCreateView.as_view()),
    path("questions/<int:pk>/",QuestionRetrieveUpdateDeleteView.as_view()),
    path("submission/",SubmissionListCreateView.as_view()),
    path("submission/<int:pk>/",SubmissionRetrieveUpdateDeleteView.as_view()),
    path("submission/<int:pk>/evaluate",EvaluateSubmissionView.as_view()),

    
]
