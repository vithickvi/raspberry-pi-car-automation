from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from carcontrol import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^start/', TemplateView.as_view(template_name='start.html')),
	url(r'^updatemotor/', views.processit),
]
