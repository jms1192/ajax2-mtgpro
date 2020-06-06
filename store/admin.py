from django.contrib import admin
from .models import store_user, store_event_post, store_promotion_post, follow_store
# Register your models here.

admin.site.register(store_user)
admin.site.register(store_promotion_post)
admin.site.register(store_event_post)
admin.site.register(follow_store)