from django.urls import path
from .import views

# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('',include('Base.urls')),
# ]


urlpatterns = [
     path('',views.contact)
]
