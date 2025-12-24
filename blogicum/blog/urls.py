from django.urls import include, path  # type: ignore[import-untyped]

from . import views

app_name: str = 'blog'

post_id_patterns: list[path] = [
    path('', views.PostPageView.as_view(), name='post_detail'),
    path('edit/', views.PostEditView.as_view(), name='edit_post'),
    path('comment/', views.CommentAddView.as_view(),
         name='add_comment'),
    path('edit_comment/<int:comment_id>/',
         views.CommentEditView.as_view(), name='edit_comment'),
    path('delete/', views.PostRemoveView.as_view(),
         name='delete_post'),
    path('delete_comment/<int:comment_id>/',
         views.CommentRemoveView.as_view(), name='delete_comment'),
]

urlpatterns: list[path] = [
    path('', views.MainPageView.as_view(), name='index'),
    path('category/<slug:category_slug>/', views.CategoryPageView.as_view(),
         name='category_posts'),
    path('profile/edit/', views.ProfileEditView.as_view(),
         name='edit_profile'),
    path('profile/<slug:name_slug>/', views.ProfilePageView.as_view(),
         name='profile'),
    path('posts/create/', views.PostAddView.as_view(), name='create_post'),
    path('posts/<int:post_id>/', include(post_id_patterns)),
]
