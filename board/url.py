from django.urls import path
from . import views



urlpatterns = [

    path('', views.top_list, name='index'),
    # path('<int:id>/', views.base, name='base'),

    path('boards/<int:id>/', views.boards_topic, name='boards_topic'),

    #
    path('up_imge/', views.Up_imge, name='up_imge'),
    path('detail/<int:id>/', views.topic_detail, name='detail'),
    path('new/', views.TopicCreate.as_view(), name='new_topic'),


    path('detail/<int:pk>/update/', views.TopicUpdate.as_view(), name='update'),
    path('detail/<int:pk>/delete/', views.TopicDelete.as_view(), name='delete'),

    path('boards/top_list', views.top_list, name='top_list'),
    path('user_topics/<int:id>/', views.designer_works, name='user_topics'),




]