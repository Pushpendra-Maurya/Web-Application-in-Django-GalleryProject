from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view.as_view(), name='home'),
    path('register/',views.register_view.as_view(), name='register'),
    path('signout/',views.signout_view, name='signout'),
    path('gallery/',views.gallery_view.as_view(), name='gallery'),
    path('addimage/',views.addimage_view.as_view(), name='addimage'),
    path('myupload/',views.MyUpload_View.as_view(), name='myupload'),
    path('cat/<int:id>/',views.Cat_View.as_view(), name='cat'),
    path('viewinfo/<int:id>/',views.View_Info.as_view(), name='viewinfo')

]