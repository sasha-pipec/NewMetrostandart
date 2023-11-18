from django.urls import path
from metrostandart_app.views.pages import (HomePageRenderView,
                                           AuthorizationPageRenderView, RegistrationPageRenderView,
                                           user_logout)

urlpatterns = [
    # Pages
    path('', HomePageRenderView.as_view(), name='home'),
    path('auth/', AuthorizationPageRenderView.as_view(), name='login'),
    path('register/', RegistrationPageRenderView.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
]
