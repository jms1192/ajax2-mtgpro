from django.shortcuts import render, redirect
from home.models import decks, cards_in_deck, UserProfile, cards, follow_modle
from django.contrib.auth.models import User
from .forms import follow_form, follow_store_form
from django.views import View
from store.models import store_user, store_promotion_post, store_event_post, follow_store
#this gets the data for the home page of the user 
def user_home(request):
    #deck_list
    current_user = UserProfile.objects.filter(user = request.user)
    try:
        deck_list = decks.objects.filter(deck_creator = current_user[0])   
    except: 
        deck_list = None
    #add_deck eveythin below needs work that is the problem
    return render(request, 'user_social/user_home.html', {'deck_list': deck_list})

#this loads the socail page for a user 


class social_home1(View):

    def get(self, request):

        form = follow_form()
        form1 = follow_store_form()

        name_list = []
        current_user = (UserProfile.objects.filter(user=request.user))[0]
        people_following = (follow_modle.objects.filter(follower=current_user))
        for i in people_following:
            name_list.append(i.followed)
    
    
        decklist = decks.objects.filter(deck_publish = True) 
        for i in name_list:
            decklist = decklist.exclude(deck_creator = i)
    
        deck_list2 = []
        deck_list = decks.objects.filter(deck_publish = True)
        for i in deck_list:
            if not i in decklist:
                deck_list2.append(i)

        following = len(people_following)
        followers = len(follow_modle.objects.filter(followed=current_user))
        shops_following = len(follow_store.objects.filter(follower=current_user))

        stores_following = follow_store.objects.filter(follower=current_user)
        store_events = []
        store_promotions = []
        for i in stores_following:
            events = store_event_post.objects.filter(store=(i.store))
            for j in events:
                store_events.append(j)
            promotions = store_promotion_post.objects.filter(store=(i.store))
            for k in promotions:
                store_promotions.append(k)
        
        return render(request, 'user_social/social_home.html', {'decklist': deck_list2, 'following': following, 'followers': followers, 'user': current_user, 'form': form, 'store_events': store_events, 'store_promotions': store_promotions, 'form1': form1, 'shops_following': shops_following}) 

    def post(self, request):

        form1 = follow_store_form(request.POST)
        form = follow_form(request.POST)

        if form.is_valid():
            user_following_username = form.cleaned_data.get("follow")
            follower1 = (UserProfile.objects.filter(user=request.user))[0]
            try:
                user_following = (User.objects.filter(username=user_following_username))[0]
                user_following = (UserProfile.objects.filter(user=user_following))[0]
                test = 0 
            except:
                test = 1
            if test == 0:
                new_follow = follow_modle(follower=follower1, followed=user_following)
                test2 = str(follow_modle.objects.filter(follower=follower1).filter(followed=user_following))
                if test2 == '<QuerySet []>':
                    new_follow.save()

        
        if form1.is_valid():
            user = (UserProfile.objects.filter(user=request.user))[0]
            store_name = form1.cleaned_data.get("store_name")
            try:
                store = (store_user.objects.filter(store_name=store_name))[0]
                fail = False
            except:
                fail = True
            if not fail == True:    
                test3 = str(follow_store.objects.filter(store=store).filter(follower=user))
                if test3 == '<QuerySet []>':
                    follow = follow_store(store=store, follower=user)
                    follow.save()
        return redirect('http://localhost:8000/user_social/social_home')



#this loads a page of all the followers or the people following a user
# 

def follow_list(request, id, kind):
        
    if kind == 'followers':
        name_list = []
        current_user = (UserProfile.objects.filter(id=id))[0]
        followers = (follow_modle.objects.filter(followed=current_user))
        for i in followers:
            name_list.append(i.follower)
    else:
        name_list = []
        current_user = (UserProfile.objects.filter(id=id))[0]
        people_following = (follow_modle.objects.filter(follower=current_user))
        for i in people_following:
            name_list.append(i.followed)
            
        #could probaby shorten this code
    
    return render(request,'user_social/follow_list.html', {'name_list': name_list, 'user': current_user, 'kind': kind})

#this shows the profile page of other users 
def other_player_profile(request, id):

    user = (UserProfile.objects.filter(id =id))[0]
    if user == (UserProfile.objects.filter(user=request.user))[0]:
        return redirect('/user_social/social_home')
        
    else:
        people_following = len(follow_modle.objects.filter(follower=user))
        followers = len(follow_modle.objects.filter(followed=user))
        decks1 = decks.objects.filter(deck_publish = True).filter(deck_creator = user)

        return render(request, 'user_social/other_player_profile.html', {'decks1': decks1, 'user': user, 'people_following': people_following,'followers':followers})