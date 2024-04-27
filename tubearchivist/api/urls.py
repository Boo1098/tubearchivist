"""all api urls"""

from api import views
from django.urls import path

urlpatterns = [
    path("ping/", views.PingView.as_view(), name="ping"),
    path("login/", views.LoginApiView.as_view(), name="api-login"),
    path(
        "video/",
        views.VideoApiListView.as_view(),
        name="api-video-list",
    ),
    path(
        "video/<slug:video_id>/",
        views.VideoApiView.as_view(),
        name="api-video",
    ),
    path(
        "video/<slug:video_id>/progress/",
        views.VideoProgressView.as_view(),
        name="api-video-progress",
    ),
    path(
        "video/<slug:video_id>/comment/",
        views.VideoCommentView.as_view(),
        name="api-video-comment",
    ),
    path(
        "video/<slug:video_id>/similar/",
        views.VideoSimilarView.as_view(),
        name="api-video-similar",
    ),
    path(
        "video/<slug:video_id>/sponsor/",
        views.VideoSponsorView.as_view(),
        name="api-video-sponsor",
    ),
    path(
        "video/<slug:video_id>/mp3/",
        views.VideoMP3View.as_view(),
        name="api-video-mp3",
    ),
    path(
        "channel/",
        views.ChannelApiListView.as_view(),
        name="api-channel-list",
    ),
    path(
        "channel/search/",
        views.ChannelApiSearchView.as_view(),
        name="api-channel-search",
    ),
    path(
        "channel/<slug:channel_id>/",
        views.ChannelApiView.as_view(),
        name="api-channel",
    ),
    path(
        "channel/<slug:channel_id>/video/",
        views.ChannelApiVideoView.as_view(),
        name="api-channel-video",
    ),
    path(
        "playlist/",
        views.PlaylistApiListView.as_view(),
        name="api-playlist-list",
    ),
    path(
        "playlist/<slug:playlist_id>/",
        views.PlaylistApiView.as_view(),
        name="api-playlist",
    ),
    path(
        "playlist/<slug:playlist_id>/video/",
        views.PlaylistApiVideoView.as_view(),
        name="api-playlist-video",
    ),
    path(
        "download/",
        views.DownloadApiListView.as_view(),
        name="api-download-list",
    ),
    path(
        "download/<slug:video_id>/",
        views.DownloadApiView.as_view(),
        name="api-download",
    ),
    path(
        "refresh/",
        views.RefreshView.as_view(),
        name="api-refresh",
    ),
    path(
        "snapshot/",
        views.SnapshotApiListView.as_view(),
        name="api-snapshot-list",
    ),
    path(
        "snapshot/<slug:snapshot_id>/",
        views.SnapshotApiView.as_view(),
        name="api-snapshot",
    ),
    path(
        "backup/",
        views.BackupApiListView.as_view(),
        name="api-backup-list",
    ),
    path(
        "backup/<str:filename>/",
        views.BackupApiView.as_view(),
        name="api-backup",
    ),
    path(
        "task-name/",
        views.TaskListView.as_view(),
        name="api-task-list",
    ),
    path(
        "task-name/<slug:task_name>/",
        views.TaskNameListView.as_view(),
        name="api-task-name-list",
    ),
    path(
        "task-id/<slug:task_id>/",
        views.TaskIDView.as_view(),
        name="api-task-id",
    ),
    path(
        "config/user/",
        views.UserConfigView.as_view(),
        name="api-config-user",
    ),
    path(
        "cookie/",
        views.CookieView.as_view(),
        name="api-cookie",
    ),
    path(
        "watched/",
        views.WatchedView.as_view(),
        name="api-watched",
    ),
    path(
        "search/",
        views.SearchView.as_view(),
        name="api-search",
    ),
    path(
        "token/",
        views.TokenView.as_view(),
        name="api-token",
    ),
    path(
        "notification/",
        views.NotificationView.as_view(),
        name="api-notification",
    ),
    path(
        "stats/video/",
        views.StatVideoView.as_view(),
        name="api-stats-video",
    ),
    path(
        "stats/channel/",
        views.StatChannelView.as_view(),
        name="api-stats-channel",
    ),
    path(
        "stats/playlist/",
        views.StatPlaylistView.as_view(),
        name="api-stats-playlist",
    ),
    path(
        "stats/download/",
        views.StatDownloadView.as_view(),
        name="api-stats-download",
    ),
    path(
        "stats/watch/",
        views.StatWatchProgress.as_view(),
        name="api-stats-watch",
    ),
    path(
        "stats/downloadhist/",
        views.StatDownloadHist.as_view(),
        name="api-stats-downloadhist",
    ),
    path(
        "stats/biggestchannels/",
        views.StatBiggestChannel.as_view(),
        name="api-stats-biggestchannels",
    ),
]
