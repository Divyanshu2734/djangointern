
from django.urls import path,include
from authapp import views
urlpatterns = [
   
    path('signup/',views.signup, name="signup" ),
    path('login/',views.signin, name="signin" ),
    path('signout/',views.signout, name="signout" ),
    path('doctor/',views.doctor, name="dr" ),
    path('patient/',views.patient, name="p" ),
    path('',views.base, name="b" ),
]