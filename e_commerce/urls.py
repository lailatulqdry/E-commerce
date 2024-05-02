from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dyMall import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/kategori/', views.kategori_list),
    path('api/kategori/<int:pk>/', views.KategoriDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
