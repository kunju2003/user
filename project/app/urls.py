from django.urls import path
from . import views
urlpatterns=[
    path('',views.userlog),
    path('userhome',views.userhome),
    path('userreg',views.userreg),
    path('adminlog',views.adminlog),
    path('adminhome',views.adminhome),
    path('userlogout',views.userlogout),
    path('adminlogout',views.adminlogout)
]