from django.urls import path
from . import views

urlpatterns = [


    #!  ACCOUNTS -register paths 
    path('account/', views.getAllAccounts),
    path('account/<int:id>/', views.getSingleAccount),
    path('account/register/', views.registerAccount),  #add
    path('account/resetAccount/<int:id>/', views.resetAccount),  #update , (use for reset password)
    path('account/delete/<int:id>/', views.deleteAccount),    #delete

    #! MEMBER PROFILE DATA paths ( here uid prop is setted as primary key)
    path('memberProfile/', views.getMemberProfile),
    path('memberProfile/<int:id>/', views.getSingleMemberProfile),
    path('memberProfile/add/', views.addMemberProfile),
    path('memberProfile/update/<int:id>/', views.updateMemberProfile),
    path('memberProfile/delete/<int:id>/', views.deleteMemberProfile),
   
    #! GYM TRACK  paths ( here uid prop id setted as primary key)
    path('gymTrack/', views.getGymTrack),
    path('gymTrack/<int:id>/', views.getSingleGymTrack),
    path('gymTrack/add/', views.addGymTrack),
    path('gymTrack/update/<int:id>/', views.updateGymTrack),
    path('gymTrack/delete/<int:id>/', views.deleteGymTrack),
    path('gymTrack/deleteByUid/<int:uid>/', views.deleteGymTrackByUid), # delete by uid ( dont need now as uid=id)


]