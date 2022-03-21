import django_filters
from .models import * 

class AccountFilters(django_filters.FilterSet):
    class Meta: 
        model = AuthUser
        fields = '__all__'

class GymTrackFilters(django_filters.FilterSet):
    class Meta: 
        model = GymTrack
        fields = '__all__'
#         # fields = ['recordDate', 'g_uid']