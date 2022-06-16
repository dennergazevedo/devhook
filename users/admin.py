from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserCreationForm, UserChangeForm
from .models import Users

@admin.register(Users)
class UserAdmin(auth_admin.UserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm
  model = Users