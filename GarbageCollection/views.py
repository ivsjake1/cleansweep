from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Collection, PostNews, CreatePickup, Header, Goal, Waste, PostEvent, FooterBusinessHours, UserInfo, Footer
from .forms import PickupForm, UserProfileForm, UserInfoForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import HeaderFrom


def index(request):
    context = {}

    try:
        headers = Header.objects.latest('id')
    except ObjectDoesNotExist:
        headers = None

    try:
        goals = Goal.objects.latest('id')
    except ObjectDoesNotExist:
        goals = None

    news = PostNews.objects.all().order_by('-post_date')
    wastes = Waste.objects.all()

    try:
        events = PostEvent.objects.latest('id')
    except ObjectDoesNotExist:
        events = None

    business_hours = FooterBusinessHours.objects.all()

    try:
        footer = Footer.objects.latest('id')
    except ObjectDoesNotExist:
        footer = None

    total_pickup_list = CreatePickup.objects.filter(status='Complete').count()
    pickup_list = CreatePickup.objects.filter(status='Pending').count()
    pickup_work = CreatePickup.objects.filter(status='On The Way').count()

    context = {
        'headers': headers,
        'goals': goals,
        'news': news,
        'wastes': wastes,
        'events': events,
        'business_hours': business_hours,
        'footer_data': footer,
        'total_pickup_list': total_pickup_list,
        'pickup_list': pickup_list,
        'pickup_work': pickup_work
    }

    return render(request, 'home.html', context)


def collection(request):
    collection = Collection.objects.all()
    context = {'show_collection': collection}
    return render(request, 'collection.html', context)


def news(request):
    news = PostNews.objects.all().order_by('-post_date')
    return render(request, 'news.html', {'show_news': news})


def news_detail(request, id):
    try:
        news = PostNews.objects.get(id=id)
        context = {'news': news}
        return render(request, 'news_detail.html', context)
    except PostNews.DoesNotExist:
        return render(request, 'error_page.html')


def pickup(request):
    user = request.user

    context = {}
    form = PickupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Waste Pickup Requested...")
        return redirect('pickup')

    context['form'] = form
    return render(request, 'pickup.html', context)


def pickup_details(request, id):
    try:
        pickup = CreatePickup.objects.get(id=id)
        pickup.is_read = True  # Mark the pickup as read
        pickup.save(update_fields=['is_read'])  # Save only the 'is_read' field
        context = {'data': pickup}
        return render(request, 'pickup_details.html', context)
    except CreatePickup.DoesNotExist:
        return render(request, 'error_page.html')



def pickup_list(request):
    user = request.user
    if not user.is_authenticated:
        context = {'pickuplist': None}
        return render(request, 'pickup_list.html', context)


    pickuplist = CreatePickup.objects.filter(user=request.user).filter(status='Pending',).order_by('-date')
    moving = CreatePickup.objects.filter(user=request.user).filter(status='On The Way',).count()
    current_user = request.user
    complete_pickup_list = CreatePickup.objects.filter(user=request.user, status='Complete').count()
    pending_pickup_list = CreatePickup.objects.filter(user=request.user, status='Pending').count()
    return render(request, 'pickup_list.html', {'show_list': pickuplist, 'current_user': current_user,
                 'complete_pickup_list': complete_pickup_list,
                                                'pending_pickup_list': pending_pickup_list, 'moving':moving})

def pickup_list_complete(request):
    pickuplist = CreatePickup.objects.filter(user=request.user).filter(status='Complete',).order_by('-date')
    moving = CreatePickup.objects.filter(user=request.user).filter(status='On The Way',).count()
    current_user = request.user
    complete_pickup_list = CreatePickup.objects.filter(user=request.user, status='Complete').count()
    pending_pickup_list = CreatePickup.objects.filter(user=request.user, status='Pending').count()
    return render(request, 'pickup_list_complete.html', {'show_list': pickuplist, 'current_user': current_user,
                 'complete_pickup_list': complete_pickup_list,
                                                'pending_pickup_list': pending_pickup_list, 'moving':moving})

def pickup_list_ontheway(request):
    pickuplist = CreatePickup.objects.filter(user=request.user).filter(status='On The Way',).order_by('-date')
    moving = CreatePickup.objects.filter(user=request.user).filter(status='On The Way',).count()
    current_user = request.user
    complete_pickup_list = CreatePickup.objects.filter(user=request.user, status='Complete').count()
    pending_pickup_list = CreatePickup.objects.filter(user=request.user, status='Pending').count()
    return render(request, 'pickup_list_ontheway.html', {'show_list': pickuplist, 'current_user': current_user,
                  'complete_pickup_list': complete_pickup_list,
                                                'pending_pickup_list': pending_pickup_list, 'moving':moving})





@login_required(login_url="login")
def profile(request):
    user = request.user
    try:
        user_info = UserInfo.objects.latest('id')
    except UserInfo.DoesNotExist:
        user_info = None


    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)

        if user_form.is_valid() :
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserProfileForm(instance=user)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'user_info':user_info})


@login_required(login_url="login",)
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed...')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile.html', {'form': form})


@login_required(login_url="login",)
def add_address(request):
    user = request.user
    form = UserInfoForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('profile')

    context = {
        'form': form
    }

    return render(request, 'profile.html', context)


def edit_address(request):
    try:
        user = request.user
        user_info = UserInfo.objects.latest('id')
    except UserInfo.DoesNotExist:
        user_info = None

    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('profile')
    else:
        form = UserInfoForm(instance=user_info)

    context = {
        'form': form,
        'user_info': user_info,
    }
    return render(request, 'profile.html', context)


def delete_request(request, id):
    request = CreatePickup.objects.get(id=id)
    request.delete()
    return redirect('pickup_list')
