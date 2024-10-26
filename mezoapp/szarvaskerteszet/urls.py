from django.contrib import admin
from django.urls import path
from szarvaskerteszet.views import Introduction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Introduction.as_view(), name='intro' ),
]