from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('community/', views.community, name='community'),
    path('computers/<int:computer_id>/', views.computer_detail, name='computer-detail'),
    path('computers/create/', views.ComputerCreate.as_view(), name='computer-create'),
    path('computers/<int:pk>/update/', views.ComputerUpdate.as_view(), name='computer-update'),
    path('computers/<int:pk>/delete/', views.ComputerDelete.as_view(), name='computer-delete'),
    path('computers/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment-create'),
    path('computers/<int:computer_id>/update/<int:comment_id>/', views.CommentUpdate.as_view(), name='comment-update'),
    path('computers/<int:computer_id>/delete/<int:comment_id>/', views.CommentDelete.as_view(), name='comment-delete'),
    path('computers/<int:computer_id>/createPeripherals/', views.PeripheralsCreate.as_view(), name='computer-peripherals'),
    path('computers/<int:pk>/updatePeripherals/', views.PeripheralsUpdate.as_view(), name='computer-peripherals-update'),
    path('computers/<int:pk>/deletePeripherals/', views.PeripheralsDelete.as_view(), name='computer-peripherals-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]