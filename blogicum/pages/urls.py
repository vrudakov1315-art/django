from django.urls import path  # type: ignore[import-untyped]

from . import views

app_name: str = 'pages'

urlpatterns: list[path] = [
    path('about/', views.AboutViewCBV.as_view(), name='about'),
    path('rules/', views.RulesViewCBV.as_view(), name='rules'),
]
