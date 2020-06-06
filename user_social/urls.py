from django.urls import path, include
from . import views
from .views import social_home1
#this file takes urls from the web and redirects them to the views that will exicue a function baced on the url entered
urlpatterns = [
    path('user_home', views.user_home),
    path('social_home', social_home1.as_view()),
    path('follow_page/<id>/<kind>', views.follow_list),
    path('other_player_profile/<id>', views.other_player_profile),
    
]