from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views

from accounts.views import ProfileView

urlpatterns = [
    path(
        # Прописываю отдельно этот адресс, чтобы шаблон письма брался из html
        # шаблона, а не .txt
        "password/reset/",
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy("auth_password_reset_done"),
            html_email_template_name="registration/password_reset_email.html",
        ),
        name="auth_password_reset"
    ),
    path("", include("registration.backends.default.urls")),
    path('profile/<int:username>/', ProfileView.as_view(), name='profile')
]