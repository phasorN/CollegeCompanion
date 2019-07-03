from django.contrib import admin
from django.urls import path
from django.urls import include
from expenses import views as expenses_views
from attendance import views as attendance_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('', expenses_views.api_root),
    path('users/', expenses_views.UserSelfDetailsOrCreate.as_view(), name="user-create-and-details"),
    path('users/<int:pk>/', expenses_views.UserDetail.as_view(), name="user-detail"),

    path('expenses/', expenses_views.ExpensesCreateListView.as_view(), name="expenses-create-and-list"),
    path('expenses/<int:pk>/', expenses_views.ExpensesDetail.as_view(), name="expenses-detail"),

    path('subject/', attendance_views.SubjectCreateListView.as_view(), name="subject-create-and-list"),
    path('subject/<int:pk>/', attendance_views.SubjectDetailView.as_view(), name='subject-detail'),

    path('period/', attendance_views.PeriodCreateListView.as_view(), name="period-create-and-list"),
    path('period/<int:pk>/', attendance_views.PeriodDetailView.as_view(), name="period-detail"),

    path('attendance/', attendance_views.AttendanceCreateListView.as_view(), name="attendance-create-and-list"),
    path('attendance/<int:pk>/', attendance_views.AttendanceDetailView.as_view(), name="attendance-detail"),
]
handler404 = 'expenses.views.custom404'
handler500 = 'expenses.views.custom500'
