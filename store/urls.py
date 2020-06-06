from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import store_signup, store_home, post_event, post_promotion, change_store_info, shops_following, shop_page,shop_search, shop_search_results

 
urlpatterns = [
    path('sign_up/', store_signup.as_view()),
    path('home/<s_id>/', store_home.as_view()),
    path('post_event/<s_id>/', post_event.as_view()),
    path('post_promotion/<s_id>', post_promotion.as_view()),
    path('change_info/<s_id>', change_store_info.as_view()),
    path('shops_following/', shops_following.as_view()),
    path('shop_page/<s_id>/', shop_page.as_view()),
    path('shop_search/', shop_search.as_view()),
    path('shop_search_results/<zip_code>/<distance>/', shop_search_results.as_view())


]