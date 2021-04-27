from django.urls import path
from .views import home, detail, add_user

app_name = 'visit'

urlpatterns = [
    path('', home, name="home"),
    path('<int:user_id>/', detail, name="detail"),
    path('add_user/', add_user, name="add_user"),
]
