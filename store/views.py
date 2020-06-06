from django.shortcuts import render, redirect
from django.views import View
from .forms import store_register_form, event_post, promotion_post, change_info, find_store
from .models import store_user, store_event_post, store_promotion_post, follow_store
from django.contrib.auth.models import User
from .models import UserProfile
from geopy.distance import geodesic
import zipcodes

#where stores create accounts 
class store_signup(View):

    def get(self, request):
        form = store_register_form()

        return render(request, 'store/store_signup.html', {'form':form})

    def post(self,request):

        form = store_register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password_first")
            User.objects.create_user(username, email, password)
            user = (User.objects.all())
            user = (User.objects.all())[(len(user) - 1)]


            blurb = form.cleaned_data.get("blurb_about_store")
            zip_code = form.cleaned_data.get("zip_code")
            store_name = form.cleaned_data.get("store_name")
            adress = form.cleaned_data.get("adress")
            link_store_website = form.cleaned_data.get("link_store_website")

            new_store = store_user(user=user, zip_code=zip_code, link_store_website=link_store_website, adress=adress, store_name=store_name, blurb_about_store=blurb)
            new_store.save()
            
            return redirect(('http://localhost:8000/store/home/' + str(new_store.id)))

class store_home(View):

    def get(self,request, s_id):
        store = (store_user.objects.filter(id=s_id))[0]
        events_posted = store_event_post.objects.filter(store=store)
        promotions_posted = store_promotion_post.objects.filter(store=store)

        context = {'s_id': s_id, 'store': store, 'events_posted': events_posted, 'promotions_posted': promotions_posted }


        return render(request, 'store/home.html', context)


class post_event(View):

    def get(self,request, s_id):
        form = event_post()

        return render(request, 'store/post_event.html', {'form':form, 's_id':s_id})


    def post(self, request, s_id):
        form = event_post(request.POST)
        if form.is_valid():
            
            event_title = form.cleaned_data.get("event_title")
            event_date = form.cleaned_data.get('event_date')
            event_time = form.cleaned_data.get("event_time")
            event_format = form.cleaned_data.get("event_format")
            event_discription = form.cleaned_data.get("event_discription")
            store = (store_user.objects.filter(id=s_id))[0]

            event_post1 = store_event_post(store=store, event_title=event_title, event_time=event_time, event_format=event_format, event_discription=event_discription, event_date=event_date)
            event_post1.save()

        return render(1)

class post_promotion(View):

    def get(self,request, s_id):
        form = promotion_post()

        return render(request, 'store/post_promotion.html', {'form':form, 's_id': s_id}) 

    def post(self,request, s_id):
        form = promotion_post(request.POST)
        if form.is_valid():
            
            promotion_title = form.cleaned_data.get("promotion_title")
            promotion_discription = form.cleaned_data.get("promotion_discription")
            store = (store_user.objects.filter(id=s_id))[0]

            promotion_post1 = store_promotion_post(store=store, promotion_title=promotion_title, promotion_discription=promotion_discription)
            promotion_post1.save()

        return redirect()


class change_store_info(View):

    def get(self, request, s_id):
        form = change_info()

        return render(request, 'store/change_info.html', {'form':form, 's_id': s_id})


    def post(self, request, s_id):

        form = change_info(request.POST)
        if form.is_valid():
            
            blurb = form.cleaned_data.get("blurb_about_store")
            zip_code = form.cleaned_data.get("zip_code")
            store_name = form.cleaned_data.get("store_name")
            adress = form.cleaned_data.get("adress")
            link_store_website = form.cleaned_data.get("link_store_website")

            store = (store_user.objects.filter(id=s_id))[0]

          
            store.blurb_about_store = blurb
            store.zip_code = zip_code
            store.store_name = store_name
            store.adress = adress
            store.link_store_website = link_store_website

            store.save(update_fields=['blurb_about_store', 'zip_code', 'store_name', 'adress', 'link_store_website'])

        return redirect()
#for this function i want all of the form inputs to alredy be filled in with info that the shop alredy put in             


class shop_stats(View):
     
     def get(self, retuen, s_id):
         
         return redirect()
#this is going to be the view of a page for shops that contains statistics about how many people are viewing their page clicking their link or responding to their promotions.

#this is how users find the a list of shops that they are following and they can look at each shops page.
class shops_following(View):
    
    def get(self, request):

        user = (UserProfile.objects.filter(user=request.user))[0]
        shop_list = [i.store for i in follow_store.objects.filter(follower=user)]

        context = { 'shop_list': shop_list}

        return render(request, 'store/shops_following.html', context)


#this loads the page where shops display a page to users 
class shop_page(View):
    
    def get(self, request, s_id):
        shop = (store_user.objects.filter(id=s_id))[0]
        promotion_list = store_promotion_post.objects.filter(store=shop)
        event_list = store_event_post.objects.filter(store=shop)

        context = {'shop': shop, 'promotion_list': promotion_list, 'event_list': event_list}
        if request.user.is_active == True:
            return render(request, 'store/user_shop_page.html', context)
        else:
            return render(request, 'store/shop_page.html', context)


class shop_search(View):

    def get(self, request):
        form = find_store()
        if request.user.is_active == True:
            return render(request, 'store/user_shop_search.html', {'form': form})
        else:
            return render(request, 'store/shop_search.html', {'form': form})

    def post(self,request):
        form = find_store(request.POST)
        if form.is_valid():
            zip_code = form.cleaned_data.get('zip_code')
            distance_in_miles = form.cleaned_data.get('distance_in_miles')
            return redirect('http://localhost:8000/store/shop_search_results/' + str(zip_code) + '/' + str(distance_in_miles) + '/')



class shop_search_results(View):
    
    def get(self, request, zip_code, distance):

        location = zipcodes.matching(zip_code)
        lat1 = float((location[0])['lat'])
        long1 = float((location[0])['long'])
        current_coordinate = (lat1,long1)
        store_list = []
        if not location == []:
            for i in store_user.objects.all():
                zip_code2 = i.zip_code
                location2 = zipcodes.matching(zip_code2)
                if not location2 == []:
                    lat2 = float((location2[0])['lat'])
                    long2 = float((location2[0])['long'])
                    shop_coordinate = (lat2,long2)
                    distance2 = geodesic(current_coordinate, shop_coordinate).miles
                    distance = float(distance)
                    if distance2 <= distance:
                        store_list.append([i, distance2])

        store_list = sorted(store_list,key=lambda l:l[1])

        if request.user.is_active == True:
            return render(request, 'store/user_search_results.html', {'store_list': store_list})
        else:
            return render(request, 'store/search_results.html', {'store_list': store_list})

        
