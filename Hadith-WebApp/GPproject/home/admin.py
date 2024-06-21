from django.contrib import admin


from .models import Login
from .models import Answer

admin.site.register(Login)

admin.site.register(Answer)