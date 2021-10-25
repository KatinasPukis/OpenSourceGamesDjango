from django.contrib import admin
from .models  import Comment, Customer , UserGame , NewsClass
# Register your models here.
admin.site.register(Customer),
admin.site.register(UserGame),
admin.site.register(NewsClass),
admin.site.register(Comment),