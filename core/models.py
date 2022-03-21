from django.db import models

# Create your models here.
class AuthUser(models.Model):
    email = models.CharField(max_length=20,default="no value")
    password = models.CharField(max_length=20,default="no value")  
    isAdmin = models.BooleanField(default=False)

#! using OneToOneField , coz one account can have only profile ( user can create one rowObj of this class )
class MemberProfile(models.Model):
    name = models.CharField(max_length=30,default="no value")
    bio = models.CharField(max_length=20,default="no value")
    gender = models.CharField(max_length=20,default="no value")
    age = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default="no value")
    mobileNum =  models.IntegerField(default=1)
    dob = models.IntegerField(default=1)
    lockerNum = models.IntegerField(default=1)
    reg_no = models.IntegerField(default=1)
    membership_no = models.IntegerField(default=1)
    package = models.CharField(max_length=20,default="no value")
    startDate = models.IntegerField(default=1)
    period = models.IntegerField(default=1)
    endDate = models.IntegerField(default=1)
    isApproved = models.BooleanField(default=False)  # bool to be approved by admin
    m_uid = models.OneToOneField(AuthUser , on_delete=models.CASCADE, related_name='muid', primary_key=True) # uid setted as pk


# #! using filter method , coz one account can have multiple objects of this class
# class GymTrack(models.Model):
#     g_uid = models.ForeignKey(AuthUser , on_delete=models.CASCADE, related_name='guid') # filter search by ui
#     recordDate = models.CharField(max_length=20)   # filter search , by date to separate monthly track
#     weight = models.IntegerField(default=0)
#     height = models.IntegerField(default=0)
#     neck = models.IntegerField(default=0)
#     shoulder = models.IntegerField(default=0)
#     chest = models.IntegerField(default=0)
#     upperArm = models.IntegerField(default=0)
#     forearm = models.IntegerField(default=0)
#     upperAbdomen = models.IntegerField(default=0)
#     lowerAbdomen = models.IntegerField(default=0)
#     waist = models.IntegerField(default=0)
#     hips = models.IntegerField(default=0)
#     thighs = models.IntegerField(default=0)
#     calf = models.IntegerField(default=1)


