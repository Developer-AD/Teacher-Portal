from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),

    # ---------------------------- Category URLs ------------------------------
    # path('category/', views.category, name='category'),
    # path('category/<int:pk>/update/', views.category_update, name='category_update'),
    # path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
]