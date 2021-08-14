
from django.urls import path
from .views import *


urlpatterns = [
  # path('login-auth', login_auth, name='login_auth'),
   path('signup', signup, name='signup'),
   path('login-auth', loginauth, name='loginauth'),
   path('verify', verify, name='verify'),
   path('verifysuccess', verifysuccess, name='verifysuccess'),
   path('verify-email<email_tok>', verifyemail, name='verifyemail'),
   path('logout/' , logout_attempt , name="logut")
]