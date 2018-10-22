from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import (
		CreateView,
		UpdateView,
		DeleteView,

		)



from . models import Track


class IndexView(generic.ListView):
	model 			 = Track
	template_name 	 = 'track/index.html'

	def get_queryset(self):
		return Track.objects.all()


class DetailView(generic.DetailView):
	model 			= Track
	template_name   =  'track/detail.html'


class CreateView(CreateView):
	model  = Track
	template_name = 'track/track_create.html'
	fields =['track_name','track_file', 'genre', 'tags']
