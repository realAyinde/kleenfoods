from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.UserListView.as_view()),
    path('signup', views.register, name='signup'),
    
]

# urlpatterns = [
#     path('', views.UserViewSet)
# ]
