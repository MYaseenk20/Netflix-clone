from django.shortcuts import render
from django.views.generic import ListView,DetailView,YearArchiveView
from .models import Movie,MovieLinks
# Create your views here.
class movie_detail(ListView):
    model = Movie
    template_name = 'netflix/movie_list.html'
    context_object_name = 'movies'


class Homeview(ListView):
    model = Movie
    template_name = 'netflix/home.html'
    def get_context_data(self, **kwargs):
        context=super(Homeview, self).get_context_data(**kwargs)
        context['recently_added']=MovieLinks.objects.filter(status='RA')
        context['most_watches']=MovieLinks.objects.filter(status='MW')
        context['top_rated']=MovieLinks.objects.filter(status='TR')
        return context


class movie_list(DetailView):
    model = Movie
    def get_object(self):
        object=super(movie_list, self).get_object()
        object.view_count += 1
        object.save()
        return object
    def get_context_data(self, **kwargs):
        context=super(movie_list, self).get_context_data(**kwargs)
        context['links']=MovieLinks.objects.filter(movie=self.get_object())
        context['related_movies']=Movie.objects.filter(category=self.get_object().category)
        return context
    template_name = 'netflix/movie_detail.html'

class MovieCategory(ListView):
    model = Movie
    context_object_name = 'movies'
    def get_queryset(self):
        self.category=self.kwargs['category']
        return Movie.objects.filter(category=self.category)
    def get_context_data(self, **kwargs):
        context=super(MovieCategory,self).get_context_data(**kwargs)
        context['movie_category']=self.category
        return context
    template_name = 'netflix/movie_list.html'

class MovieLanguage(ListView):
    model = Movie
    context_object_name = 'movies'
    def get_queryset(self):
        self.language=self.kwargs['lang']
        return Movie.objects.filter(language=self.language)
    def get_context_data(self, **kwargs):
        context=super(MovieLanguage,self).get_context_data(**kwargs)
        context['movie_language']=self.language
        return context
    template_name = 'netflix/movie_list.html'

class MovieSearch(ListView):
    model = Movie
    def get_queryset(self):
        query=self.request.GET.get('query')
        if query:
            object_list=self.model.objects.filter(title__icontains=query)
        else:
            object_list=self.model.objects.none()
        return object_list
    template_name = 'netflix/movie_list.html'

class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True
    template_name = 'netflix/movie_list.html'
