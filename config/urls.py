from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi







schema_view = get_schema_view(
   openapi.Info(
      title="WIT digital recorder",
      default_version='v1',


   ),
   public=True,
)


urlpatterns = [
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/card/', include('applications.product_card.urls')),
    path('api/v1/', include('applications.courses.urls')),
    path('api/v1/', include('applications.balance.urls')),
    path('api/v1/course/buy/', include('applications.buy_courses.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
