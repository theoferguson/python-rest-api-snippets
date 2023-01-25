# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
# })

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/',
#         snippet_list,
#         name='snippet_list'),
#     path('snippets/<int:pk>',
#         snippet_detail,
#         name='snippet_detail'),
#     path('snippets/<int:pk>/highlight',
#         snippet_highlight,
#         name='snippet_highlight'),
#     path('users/',
#         user_list,
#         name='user_list'),
#     path('snippets/<int:pk>',
#         user_detail,
#         name='user_detail'),
# ])

# create a router with views
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# API URLS are now handled by the router
urlpatterns = [
    path('', include(router.urls))
]