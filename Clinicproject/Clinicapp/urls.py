from django.urls import path
from . import views

urlpatterns = [
    path('admin_list/', views.admin_list, name='admin_list'),
    path('create/', views.create_admin, name='create_admin'),
    path('edit/<int:admin_id>/', views.edit_admin, name='edit_admin'),
    path('delete/<int:admin_id>/', views.delete_admin, name='delete_admin'),
    path('',views.indexpage,name="indexpage"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('departmentpage/',views.departmentpage,name="departmentpage"),
    path('savedepartment/',views.savedepartment,name="savedepartment"),
    path('displaydepartment/',views.displaydepartment,name="displaydepartment"),
    path('editdepartment/<int:dataid>', views.editdepartment, name="editdepartment"),
    path('updatedepartment/<int:dataid>', views.updatedepartment, name="updatedepartment"),
    path('deletedepartment/<int:dataid>', views.deletedepartment, name="deletedepartment"),
    path('doctorspage/', views.doctorspage, name="doctorspage"),
    path('doctorssave/', views. doctorssave, name="doctorssave"),
    path('displaydoctors/', views.displaydoctors, name="displaydoctors"),
    path('editdoctors/<int:dataid>', views.editdoctors, name="editdoctors"),
    path('updatedoctors/<int:dataid>', views.updatedoctors, name="updatedoctors"),
    path('deletedoctors/<int:dataid>', views.deletedoctors, name="deletedoctors")

]
