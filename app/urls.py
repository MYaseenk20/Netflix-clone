from django.urls import path
from .views import movie_detail,movie_list,MovieCategory,MovieLanguage,MovieSearch,MovieYear,Homeview
app_name='app'
urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('movies/',movie_detail.as_view(),name='movie_detail'),
    path('movie/<slug:slug>/', movie_list.as_view(), name='movie_list'),
    path('category/<str:category>/', MovieCategory.as_view(), name='movie_category'),
    path('lang/<str:lang>/', MovieLanguage.as_view(), name='movie_language'),
    path('Search/', MovieSearch.as_view(), name='movie_search'),
    path('year/<int:year>/',MovieYear.as_view(), name='movie_year'),

]
