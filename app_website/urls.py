from django.urls import path

from app_website.views import HomeView, AboutView, ShopView, ServicesView, ProjectsView, BlogView, ContactView, FaqView, \
    ShopDetailView, ServicesDetailView, BlogDetailsView, BlockDetailView

app_name = 'app_website'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/category/<int:pk>/', ShopView.as_view(), name='shop-category'),
    path('services/', ServicesView.as_view(), name='services'),
    path('detail/<int:pk>/', ServicesDetailView.as_view(), name='service-detail'),
    path('shop/detail/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('block/detail/<int:pk>/', BlockDetailView.as_view(), name='block-detail'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blogdetails/', BlogDetailsView.as_view(), name='blogdetails'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
]
