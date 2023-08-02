from django.urls import path
from Frontend import views
urlpatterns=[
  path('',views.homepage,name="homepage"),
  path('deppage/', views.deppage, name="deppage"),
  path('docpage/',views.docpage,name="docpage"),
  path('appointmentpage/',views. appointmentpage,name="appointmentpage"),
  path('saveappointment/',views.saveappointment,name="saveappointment"),
  path('signuppage/',views.signuppage,name="signuppage"),
  path('savesignup/',views.savesignup,name="savesignup"),
  path('userlogin/',views.userlogin,name="userlogin"),
  path('userlogout/',views.userlogout, name="userlogout")



]