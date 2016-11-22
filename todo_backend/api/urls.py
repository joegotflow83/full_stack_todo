from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^auth/login/$', views.UserLogin.as_view({'post': 'verify'}), name='auth_token'),
    url(r'^auth/signup/$', views.UserSignup.as_view({'get': 'list', 'post': 'register'}), name='signup'),
    url(r'^users/(?P<pk>\d+)/$', views.RetrieveUpdateUserAPIView.as_view(), name='ru_user'),
    url(r'^users/(?P<pk>\d+)/tasks/$', views.ListCreateTasksAPIView.as_view(), name='lc_tasks'),
    url(r'^users/(?P<user>\d+)/tasks/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyTaskAPIView.as_view(), name='rud_task'),
    url(r'^tasks/search', views.TaskSearch.as_view({'get': 'list'}), name='task_search_name'),
    # url(r'^tasks/search?date=(?P<date>[-0-9]+)/$', views.TaskSearchDate.as_view({'get': 'list'}), name='task_search_date'),
    # url(r'^tasks/search?name=(?P<name>\w+)&date=(?P<date>[-0-9]+)/$', views.TaskSearchBoth.as_view(), name="task_search_both"),
]
