from django.urls import path
from .views import home, detail, add_user, delete_user

app_name = 'visit'

urlpatterns = [
    path('', home, name="home"),
    path('<int:user_id>/', detail, name="detail"),
    path('add_user/', add_user, name="add_user"),
    path('delete_user/<int:user_id>/', delete_user, name="delete_user"),
]
