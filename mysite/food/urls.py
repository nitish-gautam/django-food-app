from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(), name='index'),
    #/food/1
    path('<int:pk>/',views.FoodDetail.as_view(), name='detail'),
    path('item/',views.item, name='item'),
    # add items


    path('add',views.CreateItem.as_view(), name='create_item'),
    # edit
    path('update/<int:pk>/',views.update_item, name='update_item'),
    #delete
    path('delete/<int:pk>/',views.delete_item, name='delete_item'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
