from django.urls import path
from .views import CreateAccountView, UserView, AuthorView 

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('user/<int:pk>/', UserView.as_view(), name='profileview'),
    path('author/<int:pk>/', AuthorView.as_view(), name='authorview'),
]