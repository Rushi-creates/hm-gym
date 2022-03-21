from rest_framework.serializers import ModelSerializer
from core.models import *

class AuthUserSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class MemberProfileSerializer(ModelSerializer):
    class Meta : 
        model = MemberProfile
        fields = '__all__'
        # fields = [ 'id' , 'bio' , 'userName' , 'uid']

# class GymTrackSerializer(ModelSerializer):
#     class Meta:
#         model = GymTrack
#         fields = '__all__'
