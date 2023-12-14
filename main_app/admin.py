from django.contrib import admin

from .models import Dress, Review, Store, Photo

# Register your models here.
admin.site.register(Dress)
admin.site.register(Review)
admin.site.register(Store)
admin.site.register(Photo)