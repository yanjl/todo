from django.urls import path

from .views import DoListView, IndexTemplateView

app_name = 'indexes'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('list/', DoListView.as_view(), name='do_list'),
]
