from django.urls import path
from django.contrib.staticfiles.urls import serve
from .views import (
    RegistrationAPI,
    LoginAPI,
    UserAPI,
    profile_list,
    profile_detail,
    trees_list,
    tree_detail,
    notes_list,
    note_detail,
    published_trees_list,
    published_tree_detail,
    reviews_list,
    review_detail,
    changes_list,
    change_detail,
    bookmarks_list,
    bookmark_detail,
    comments_list,
    comment_detail,
    multimedia_list,
    multimedia_detail,
)


urlpatterns = [
    path("static/<path>", serve),
    path("register/", RegistrationAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("user/<int:pk>/", UserAPI.as_view()),
    path("profile/", profile_list),
    path("profile/update/", profile_detail),
    path("tree/", trees_list),
    path("tree/<int:pk>/", tree_detail),
    path("note/", notes_list),
    path("note/<int:pk>/", note_detail),
    path("published_tree/", published_trees_list),
    path("published_tree/<int:pk>/", published_tree_detail),
    path("review/", reviews_list),
    path("review/<int:pk>/", review_detail),
    path("review/", reviews_list),
    path("review/<int:pk>/", review_detail),
    path("change/", changes_list),
    path("change/<int:pk>/", change_detail),
    path("bookmark/", bookmarks_list),
    path("bookmark/<int:pk>/", bookmark_detail),
    path("comment/", comments_list),
    path("comment/<int:pk>/", comment_detail),
    path("multimedia/", multimedia_list),
    path("multimedia/<int:pk>/", multimedia_detail),
]
