from django.urls import path

from . import views



urlpatterns = [


    path('', views.IndexView.as_view(), name='index'),

    path('/create', views.CreateView.as_view(), name  = 'create'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

     path('<int:pk>/update', views.UpdateView.as_view(), name='update'),

    
]