from django.urls import path
from client.views import ai_models

API_MODULE = 'ai_models'

urlpatterns = [
    path(f'{API_MODULE}/get_model_inference', ai_models.GetModelInferenceView.as_view(), name='get_model_inference'),
    path(f'{API_MODULE}/get_model_list', ai_models.GetModelListView.as_view(), name='get_model_list')
]
