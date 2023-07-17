from django.urls import path
from . import views

urlpatterns = [
    # ... outras rotas do Django
    path('dashboard/', views.dashboard_view),
]

