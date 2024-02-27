from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('', include("QuickEditApp.urls")),
    path('admin/', admin.site.urls),
    path('grayscaling/',include("grayscaling.urls")),
    path('imageEnhancement/',include("imageEnhancement.urls")),
    path('edgeDetection/',include("edgeDetection.urls")),
    path('skewCorrection/',include("skewCorrection.urls")),
    path('textExtractor/',include("textExtractor.urls")),
    path('fileConverter/',include("fileConverter.urls")),
    path('linkShortener/',include("linkShortener.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)