from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^auth/login/$', views.UserLogin.as_view({'post': 'verify'}), name='auth_token'),
    url(r'^auth/signup/$', views.UserSignup.as_view({'get': 'list', 'post': 'register'}), name='signup'),
    url(r'^users/$', views.UserListAPIView.as_view(), name='l_users'),
    url(r'^users/(?P<pk>\d+)/$', views.RetrieveUpdateUserAPIView.as_view(), name='ru_user'),
    url(r'^users/(?P<pk>\d+)/tasks/$', views.ListCreateUserTasksAPIView.as_view(), name='lc_user_tasks'),
    url(r'^users/(?P<user>\d+)/tasks/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyUserTaskAPIView.as_view(), name='rud_task'),
    url(r'^users/(?P<pk>\d+)/add/(?P<friend_pk>\d+)/$', views.AddFriend.as_view({'post': 'add_friend'}), name="add_friend"),
    url(r'^tasks/$', views.ListCreateAllTasksAPIView.as_view(), name='lc_all_tasks'),
    url(r'^tasks/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyAllTasksAPIView.as_view(), name='lc_all_tasks'),
    url(r'^tasks/search', views.TaskSearch.as_view({'get': 'list'}), name='task_search_name'),
]
