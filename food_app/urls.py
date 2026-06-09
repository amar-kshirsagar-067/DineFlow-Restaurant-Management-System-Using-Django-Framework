from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name = 'Home'),
    path('register/', views.register, name = 'Register'),
    path('category/', views.category, name = 'Category'),
    path('category/<str:name>', views.categoryview, name = 'Category'),
    path('category/<str:cname>/<str:pname>', views.productdetail, name = 'Product_detail'),
    path('login/', views.login_page, name = 'Login'),
    path('logout/', views.logout_page, name = 'Logout'),
    path('addtocart/', views.add_to_cart, name = 'AddToCart'),
    path('cart/', views.cart_page, name = 'Cart'),
    path('removecart/<int:Cartid>', views.remove_cart, name = 'RemoveCart'),
    path('addtofav', views.add_to_fav, name = 'AddToFav'),
    path('favourite', views.favourite_page, name = 'Favourite'),
    path('removefav/<int:favid>', views.remove_fav, name = 'RemoveFav'),

   
#for the forget password urls
path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

#for the QR code urls path
path('receipt/<int:order_id>/', views.receipt_page, name='receipt_page'),
path('download-receipt/', views.generate_receipt, name='generate_receipt'),

#for the edit profile path
path('edit-profile/', views.edit_profile, name='edit_profile'),

]


    