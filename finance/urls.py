from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app.urls')),

    # path('apply-finance/', views.apply_finance),

    # # Contact Form API
    # path('contact-form/', views.contact_form),

]