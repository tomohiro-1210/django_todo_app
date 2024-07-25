# urls.py->URLやそれに対するviewフォルダの設定をする
from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete

urlpatterns = [
    path('list/', TodoList.as_view(), name="list"),
    path('detail/<int:pk>', TodoDetail.as_view(), name="detail"), #<pk>はプライマリキー
    path('create/', TodoCreate.as_view(), name="create"),
    path('delete/<int:pk>', TodoDelete.as_view(), name="delete")
]
