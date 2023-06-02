from . models import CreatePickup
def pickup_notif(request):
    if request.user.is_authenticated:
        user_pickups = CreatePickup.objects.filter(user=request.user).order_by('-last_updated')
        badge = CreatePickup.objects.filter(is_read=False, user=request.user)
    else:
        user_pickups = None
        badge = None

    return {
        'user_pickups': user_pickups,
        'badge': badge,
    }
