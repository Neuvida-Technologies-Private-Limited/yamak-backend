from django.urls import path

from client.views import connector

API_MODULE = 'connector'

urlpatterns = [
    # Access views
    path(f'{API_MODULE}/upload_data_s3', connector.UploadDataS3View.as_view(), name='upload_data_s3')
]
