from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("product/", views.product, name="product"),
    path("table1/", views.table1, name="table1"),
    path("table2/", views.table2, name="table2"),
    path("blog/", views.blog, name="blog"),

    path("add_product/", views.Add_Product, name="add_product"),

    path('change_password',views.change_password,name='change_password'),
    path('password-reset/', v.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html',subject_template_name='password_reset_email_subject.txt'),name='password_reset'),
    path('password-reset-done/', v.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', v.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', v.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    


]

