from django.urls import path
from .views import (MyAPIView, BlogListAPIView, BlogDetailAPIView,
                    ServiceListAPIView, ServiceDetailAPIView, ContactCreateAPIView,
                    PortfolioListAPIView, PortfolioDetailAPIView, SiteSettingListAPIView
        )

urlpatterns = [
    
    path("te/",MyAPIView.as_view()),
    path('blog/', BlogListAPIView.as_view(), name='blog-list'),
    path('blog/<int:id>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<int:id>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('contact/', ContactCreateAPIView.as_view(), name='contact-create'),
    path('portfolio/', PortfolioListAPIView.as_view(), name='portfolio-list'),
    path('portfolio/<int:id>/', PortfolioDetailAPIView.as_view(), name='portfolio-detail'),
    path('site-settings/', SiteSettingListAPIView.as_view(), name='site-settings-list'),

]
