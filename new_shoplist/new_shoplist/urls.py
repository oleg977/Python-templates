from django.contrib import admin
from django.urls import path  # Убедитесь, что path импортирован
from django.contrib.auth import views as auth_views  # Для работы с аутентификацией

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/', include('products.urls')),  # Подключение маршрутов приложения products
]