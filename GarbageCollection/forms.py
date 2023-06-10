from django import forms
from .models import CreatePickup, Header, User, UserInfo
from django.contrib.auth.forms import PasswordChangeForm


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ( 'city', 'barangay', 'street', 'building', 'house_no')

        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'barangay': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Barangay'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Street'}),
            'building': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
            'house_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter current password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name:
            first_name = first_name.capitalize()
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name:
            last_name = last_name.capitalize()
        return last_name


from django import forms
from .models import CreatePickup

class PickupForm(forms.ModelForm):
    class Meta:
        model = CreatePickup
        fields = ('city', 'barangay', 'street', 'building', 'house_no', 'type')

        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'barangay': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Barangay'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Street'}),
            'building': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
            'house_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
        }

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city:
            return city.capitalize()
        return city

    def clean_barangay(self):
        barangay = self.cleaned_data.get('barangay')
        if barangay:
            return barangay.capitalize()
        return barangay

    def clean_street(self):
        street = self.cleaned_data.get('street')
        if street:
            return street.capitalize()
        return street

    def clean_building(self):
        building = self.cleaned_data.get('building')
        if building:
            return building.capitalize()
        return building

    def clean_house_no(self):
        house_no = self.cleaned_data.get('house_no')
        if house_no:
            return house_no.capitalize()
        return house_no


class HeaderFrom(forms.ModelForm):
    class Meta:
        model = Header
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter text'}),
        }