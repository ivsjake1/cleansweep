from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length=50, default=None, blank=True, null=True)
    age = models.IntegerField(default=18, null=True,  blank=True,)
    contact_number = models.CharField(max_length=11, default="00000000000", null=True,  blank=True,)
    city = models.CharField(max_length=100,  default=None, blank=True, null=True)
    barangay = models.CharField(max_length=100,  default=None, blank=True, null=True)
    street = models.CharField(max_length=100,  default=None, blank=True, null=True)
    building = models.CharField(max_length=100, default=None, blank=True, null=True)
    house_no = models.CharField(max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Waste(models.Model):
    type = models.CharField(max_length=50)
    post_image = models.ImageField(null=True, blank=True, upload_to="waste_types/")
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Waste Type"


class Collection(models.Model):
    MONDAY = 'Mon'
    TUESDAY = 'Tue'
    WEDNESDAY = 'Wed'
    THURSDAY = 'Thu'
    FRIDAY = 'Fri'
    SATURDAY = 'Sat'
    SUNDAY = 'Sun'
    DayChoices = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    route = models.CharField(max_length=50, )
    city = models.CharField(max_length=50, default='Tagbilaran City')
    street = models.CharField(max_length=1000)
    schedule = MultiSelectField(choices=DayChoices, default='')
    route_image = models.ImageField(null=True, blank=True, upload_to="route_images/")
    route_link = models.CharField(max_length=5000,  blank=True, null=True)
    type = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='waste_type_1', default=None)
    type_2 = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='waste_type_2', default='',
                               blank=True, null=True)
    type_3 = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='waste_type_3', default='',
                               blank=True, null=True)
    type_4 = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='waste_type_4', default='',
                               blank=True, null=True)
    type_5 = models.ForeignKey(Waste, on_delete=models.CASCADE, related_name='waste_type_5', default='',
                               blank=True, null=True)

    class Meta:
        verbose_name_plural = "Collection Schedule"


class PostNews(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    post_date = models.DateField(auto_now_add=True)
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        verbose_name_plural = "Post News"


class CreatePickup(models.Model):
    LIQUID = 'Liquid Waste'
    SOLID = 'Solid Waste'
    ORGANIC = 'Organic Waste'
    RECYCLABLE = 'Recyclable Waste'
    HAZARDOUS = 'Hazardous waste'
    WasteTypes = [
        (LIQUID, 'Liquid Waste'),
        (SOLID, 'Solid Waste'),
        (ORGANIC, 'Organic Waste'),
        (RECYCLABLE, 'Recyclable Waste'),
        (HAZARDOUS, 'Hazardous Waste'),
    ]
    COMPLETE = 'Complete'
    PENDING = 'Pending'
    ONTHEWAY = 'On The Way'
    Status = [
        (COMPLETE, 'Complete'),
        (PENDING, 'Pending'),
        (ONTHEWAY, 'On The Way'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='pickup_request')
    date = models.DateTimeField(default=datetime.now, blank=True)
    city = models.CharField(max_length=100)
    barangay = models.CharField(max_length=100, default=None)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=100, default=None, blank=True, null=True)
    house_no = models.CharField(max_length=100, default=None, blank=True, null=True)
    type = MultiSelectField(choices=WasteTypes, default='')
    status = models.CharField(max_length=10, choices=Status, default=PENDING,)
    comment_request = models.TextField(max_length=1000, blank=True, null=True)
    remember_me = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Pickup Request"



class AutoCity(models.Model):
    auto_city = models.CharField(max_length=50)

    def __str__(self):
        return self.auto_city


class Header(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=250)


class Goal(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField(max_length=250)


class PostEvent(models.Model):
    text = models.CharField(max_length=250)
    post_image = models.ImageField(null=True, blank=True, upload_to="events/")

    class Meta:
        verbose_name_plural = "Event"


class Footer(models.Model):
    Contact1 = models.CharField(max_length=11, default="00000000000", blank=True, null=True)
    Contact2 = models.CharField(max_length=11, default="00000000000", blank=True, null=True)
    Landline = models.CharField(max_length=11, default="00000000000", blank=True, null=True)
    Address = models.CharField(max_length=50, blank=True)
    Email_us = models.CharField(max_length=50, blank=True)
    About = models.CharField(max_length=150, blank=True)
    About_innstant = models.CharField(max_length=150, blank=True)
    Facebook = models.CharField(max_length=50, blank=True)


class FooterBusinessHours(models.Model):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'
    DayChoices = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]
    Am = '12:00 AM'
    Am = '01:00 AM'
    Am = '02:00 AM'
    Am = '03:00 AM'
    Am = '04:00 AM'
    Am = '05:00 AM'
    Am = '06:00 AM'
    Am = '07:00 AM'
    Am = '08:00 AM'
    Am = '09:00 AM'
    Am = '10:00 AM'
    Am = '11:00 AM'
    TimeChoices = [
        ('Open 24 hours', 'Open 24 hours'),
        ('AM', (
            ('12:00 AM', '12:00 AM'),
            ('01:00 AM', '01:00 AM'),
            ('02:00 AM', '02:00 AM'),
            ('03:00 AM', '03:00 AM'),
            ('04:00 AM', '04:00 AM'),
            ('05:00 AM', '05:00 AM'),
            ('06:00 AM', '06:00 AM'),
            ('07:00 AM', '07:00 AM'),
            ('08:00 AM', '08:00 AM'),
            ('09:00 AM', '09:00 AM'),
            ('10:00 AM', '10:00 AM'),
            ('11:00 AM', '11:00 AM'),
         )
        ),
        ('PM', (
            ('12:00 PM', '12:00 PM'),
            ('01:00 PM', '01:00 PM'),
            ('02:00 PM', '02:00 PM'),
            ('03:00 PM', '03:00 PM'),
            ('04:00 PM', '04:00 PM'),
            ('05:00 PM', '05:00 PM'),
            ('06:00 PM', '06:00 PM'),
            ('07:00 PM', '07:00 PM'),
            ('08:00 PM', '08:00 PM'),
            ('09:00 PM', '09:00 PM'),
            ('10:00 PM', '10:00 PM'),
            ('11:00 PM', '11:00 PM'),
        )
         ),
    ]
    day = models.CharField(max_length=32, choices=DayChoices, default='')
    start_time = models.CharField(max_length=32, choices=TimeChoices,  default='Open 24 hours', blank=True, null=True)
    end_time = models.CharField(max_length=32, choices=TimeChoices, default='', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Business Hours"








