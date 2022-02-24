from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.conf.urls.static import static

from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)