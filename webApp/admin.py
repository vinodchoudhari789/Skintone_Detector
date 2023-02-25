from django.contrib import admin

from .models import ImageModel
from .models import UserProfileInfo

# admin.site.register(ImageModel)
myModels = [ImageModel, UserProfileInfo]  # iterable list
admin.site.register(myModels)
