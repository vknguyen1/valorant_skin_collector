from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='about'),
    path('skins/', views.skins_index, name='index'),
    path('skins/<int:skin_id>/', views.skins_detail, name='detail'),
    path('skins/create/', views.SkinCreate.as_view(), name='skin_create'),
    path('skins/<int:pk>/update/', views.SkinUpdate.as_view(), name='skin_update'),
    path('skins/<int:pk>/delete/', views.SkinDelete.as_view(), name='skin_delete'),
    path('skins/<int:skin_id>/add_variant/', views.add_variant, name='add_variant'),
    path('riot-account/', views.Account_Index.as_view(), name='account_index'),
    path('riot-account/create/', views.Account_Create.as_view(), name='account_create'),
    path('riot-account/<int:pk>/', views.Account_Detail.as_view(), name='account_detail'),
    path('riot-account/<int:pk>/update', views.Account_Update.as_view(), name='account_update'),
    path('riot-account/<int:pk>/delete', views.Account_Delete.as_view(), name='account_delete'),
    path('skins/<int:skin_id>/assoc_account/<int:riot_account_id>/', views.assoc_account, name='assoc_account'),
    path('accounts/signup/', views.signup, name='signup'),
]