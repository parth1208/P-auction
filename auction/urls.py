from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("product/", views.All_Products, name="product"),
    path("Products/", views.Products_table, name="Products"),
    path("Bidder/", views.Bidder, name="Bidder"),
    path("myproducts/", views.myproducts, name="myproducts"),
    path("product_details/<int:pk>", views.Product_detail, name="product_details"),
    path("done_bid/<int:pk>", views.done_bid, name="done_bid"),
    path("select_result/<int:pk>", views.select_result, name="select_result"),

    path("add_product/", views.Add_Product, name="add_product"),

    path('change_password',views.change_password,name='change_password'),
    path('password-reset/', v.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html',subject_template_name='password_reset_email_subject.txt'),name='password_reset'),
    path('password-reset-done/', v.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', v.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', v.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    


]

