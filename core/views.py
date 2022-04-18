#from appNameFolder.fileName import func/className
from core.models import   Attendance, AuthUser, GymTrack,MemberProfile
from core.myPaginations import MyCustomPagination
from core.serializers import AttendanceSerializer, AuthUserSerializer, GymTrackSerializer,MemberProfileSerializer
from .filters import AccountFilters, AttendanceFilters, GymTrackFilters 
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# ---------------------------------------------------------------------------- #
#                                   //! Auth                                   #
# ---------------------------------------------------------------------------- #

# ! (IMP) this method registers acc in DB in if account doesnt exists ( and return added obj)
# ! and logs in( means return exisiting obj ) if account already exisits 
@api_view(['POST'])
def loginOrRegister(request):
    if request.method =='POST':
        #! using get() method of py dict(to access value, by using the key), and store it in var
        myemail =request.data.get('email')
        mypass = request.data.get('password')

        #! checking if account exists in DB ( login - return exisiting acc)
        if AuthUser.objects.filter(email=myemail).exists() and AuthUser.objects.filter(password= mypass).exists() :
            #if its exists get full object based on email and pass , and return it  
            userObj = AuthUser.objects.get(email=myemail, password =mypass)
            serializer = AuthUserSerializer(instance=userObj)
            return Response(serializer.data)
        else:
             #! (IMP) if account dont exisits , then register the account(returns added acc )
             #! use this , when you want to include login & register functionality in one button 
            userObj = AuthUserSerializer(data=request.data)
            if userObj.is_valid():
                userObj.save()
                return Response(userObj.data)



@api_view(['POST'])
def loginAccount(request):
    if request.method =='POST':
        #! using get() method of py dict(to access value, by using the key), and store it in var
        myemail =request.data.get('email')
        mypass = request.data.get('password')

        #! checking if account exists in DB
        if AuthUser.objects.filter(email=myemail).exists() and AuthUser.objects.filter(password= mypass).exists() :
            #if its exists get full object based on email and pass , and return it  
            userObj = AuthUser.objects.get(email=myemail, password =mypass)
            serializer = AuthUserSerializer(instance=userObj)
            return Response(serializer.data)
        else:
            return Response(False)  # email and pass wrong



@api_view(['POST'])
def registerAccount(request):
    if request.method =='POST':
        #! using get() method of py dict(to access value, by using the key), and store it in var
        myemail =request.data.get('email')
        mypass = request.data.get('password')

        #! checking if account exists in DB
        if AuthUser.objects.filter(email=myemail).exists() and AuthUser.objects.filter(password= mypass).exists() :
            return Response(False)  # email and pass wrong
        else:
            userObj = AuthUserSerializer(data=request.data)
            if userObj.is_valid():
                userObj.save()
            return Response(userObj.data)


# @api_view(['GET'])
# def getAllAccounts(request):
#     userObj = AuthUser.objects.all()
#     filteredData = AccountFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
#     serializer = AuthUserSerializer(filteredData,many=True)
#     return Response(serializer.data)

#! with filters and pagination ( make sure to use try-except)
@api_view(['GET'])
def getAllAccounts(request):
    paginator = MyCustomPagination()
    userObj = AuthUser.objects.all()
    filteredData = AccountFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = AuthUserSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])

@api_view(['GET'])
def getSingleAccount(request,id):
    userObj = AuthUser.objects.get(id=id)
    serializer = AuthUserSerializer(instance=userObj)
    return Response(serializer.data)

@api_view(['PUT'])
def resetAccount(request,id):
    userObj = AuthUser.objects.get(id=id)
    serializers = AuthUserSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE' , 'GET'])
def deleteAccount(request,id):
    userObj = AuthUser.objects.get(id=id)
    userObj.delete()
    return Response(f"Deleted {id}")


# ---------------------------------------------------------------------------- #
#                            //! MEMBER PROFILE DATA                           #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
def addMemberProfile(request):
    userObj = MemberProfileSerializer(data=request.data)
    if userObj.is_valid():
        userObj.save()
        return Response(userObj.data)
    return Response(userObj.errors)

@api_view(['GET'])
def getMemberProfile(request):
    paginator = MyCustomPagination()
    userObj = MemberProfile.objects.all()
    try :
        context = paginator.paginate_queryset(userObj, request)
        serializer = MemberProfileSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])



#! dont need this as uid prop is setted as primary key , thus no need of filter search the uid
#! dirctly pass uid in link for update , delete
# @api_view(['GET'])
# def getMemberProfile(request):
#     userObj = MemberProfile.objects.all()
#     filteredData = MemberProfileFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
#     serializer = MemberProfileSerializer(filteredData,many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def getSingleMemberProfile(request,id):
    userObj = MemberProfile.objects.get(m_uid=id)  #! make sure to change id , to m_uid here
    serializer = MemberProfileSerializer(instance=userObj)
    return Response(serializer.data)


@api_view(['PUT'])
def updateMemberProfile(request,id):
    userObj = MemberProfile.objects.get(m_uid=id)
    serializers = MemberProfileSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)
    
@api_view(['DELETE' , 'GET'])
def deleteMemberProfile(request,id):
    userObj = MemberProfile.objects.get(m_uid=id)
    userObj.delete()
    return Response(f"Deleted by id {id}")


# dont need this here , as uid and id are the same 
# @api_view(['DELETE' , 'GET'])
# def deleteMemberProfileByUid(request,uid):
#     userObj = MemberProfile.objects.get(m_uid=uid)  #! just changed uid here 
#     userObj.delete()
#     return Response(f"Deleted by uid {uid}")


# ---------------------------------------------------------------------------- #
#                                //! GYM TRACK DB                              #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
def addGymTrack(request):
    userObj = GymTrackSerializer(data=request.data)
    if userObj.is_valid():
        print('valid')
        userObj.save()
    print(userObj.data)
    return Response(userObj.data)

# @api_view(['GET'])
# def getGymTrack(request):
#     userObj = GymTrack.objects.all()
#     serializer = GymTrackSerializer(userObj,many=True)
#     return Response(serializer.data)

# filter , ( to filter with recordData field )
@api_view(['GET'])
def getGymTrack(request):
    paginator = MyCustomPagination()
    userObj = GymTrack.objects.all()
    filteredData = GymTrackFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = GymTrackSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def getSingleGymTrack(request,id):
    userObj = GymTrack.objects.get(id=id)
    serializer = GymTrackSerializer(instance=userObj)
    return Response(serializer.data)

@api_view(['PUT'])
def updateGymTrack(request,id):
    userObj = GymTrack.objects.get(id=id)
    serializers = GymTrackSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE' , 'GET'])
def deleteGymTrack(request,id):
    userObj = GymTrack.objects.get(id=id)  #! make sure to chaneg id , to g_uid here
    userObj.delete()
    return Response(f"Deleted {id}")


# dont need this here , as uid and id are the same 
@api_view(['DELETE' , 'GET'])
def deleteGymTrackByUid(request,uid):
    userObj = GymTrack.objects.get(g_uid=uid)  #! just changed uid here 
    userObj.delete()
    return Response(f"Deleted by uid {uid}")



# ---------------------------------------------------------------------------- #
#                              //! ATTENDANCE DB                               #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
def addAttendance(request):
    userObj = AttendanceSerializer(data=request.data)
    if userObj.is_valid():
        print('valid')
        userObj.save()
    print(userObj.data)
    return Response(userObj.data)

# @api_view(['GET'])
# def getAttendance(request):
#     userObj = Attendance.objects.all()
#     serializer = AttendanceSerializer(userObj,many=True)
#     return Response(serializer.data)

# filter , ( to filter with recordData field )
@api_view(['GET'])
def getAttendance(request):
    paginator = MyCustomPagination()
    userObj = Attendance.objects.all()
    filteredData = AttendanceFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = AttendanceSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def getSingleAttendance(request,id):
    userObj = Attendance.objects.get(id=id)
    serializer = AttendanceSerializer(instance=userObj)
    return Response(serializer.data)

@api_view(['PUT'])
def updateAttendance(request,id):
    userObj = Attendance.objects.get(id=id)
    serializers = AttendanceSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE' , 'GET'])
def deleteAttendance(request,id):
    userObj = Attendance.objects.get(id=id)  #! make sure to chaneg id , to g_uid here
    userObj.delete()
    return Response(f"Deleted {id}")


# dont need this here , as uid and id are the same 
@api_view(['DELETE' , 'GET'])
def deleteAttendanceByUid(request,uid):
    userObj = Attendance.objects.get(a_uid=uid)  #! just changed uid here 
    userObj.delete()
    return Response(f"Deleted by uid {uid}")