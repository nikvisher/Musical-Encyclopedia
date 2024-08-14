from django.conf import settings # Импорт настроек проекта Django
from django.conf.urls.static import static # Импорт функции для обслуживания статических файлов в режиме разработки
from django.contrib import admin # Импорт административной панели Django
from django.urls import path, include # Импорт функций для определения маршрутов URL

urlpatterns = [
    path('admin/', admin.site.urls), # URL для административной панели Django
    path('', include('music_instruments.urls')), # URL для включения маршрутов из приложения 'music_instruments'
]

# Добавление маршрутов для обслуживания медиафайлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)