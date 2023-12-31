from .models import Post
from rest_framework.response import Response
from .serializers import PostSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import User,Group
from rest_framework.views import APIView
from rest_framework import generics,filters,permissions
from django_filters.rest_framework import DjangoFilterBackend
from media_app.tasks import send_mail_func
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import cache_page
from rest_framework.permissions import BasePermission,IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope



# Permission class
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool( request.user and request.user.is_staff)

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# GET posts ----->
class PostList(generics.ListAPIView):
    queryset=Post.objects.all().order_by('-created_on')
    serializer_class=PostSerializer
    paginate_by=10
    search_fields = ['topic']
    filter_backends = (filters.SearchFilter,)
    
    # Caching
    @method_decorator(cache_page(60*60))
    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)




# CREATE posts ----->
class PostCreate(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes = [IsAuthenticated]


# GET user accounts ----->
class UserProfileList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope] 

# CREATE user accounts ----->
class UserProfileCreate(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


# LOGIN ----->
class UserProfileLogin(APIView):
    serializer_class = UserSerializer


    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication successful
            login(request, user)  # Log in the user
            send_mail_func.delay()
            return Response({'message': 'Login successful.'}, status=200)
        else:
            # User authentication failed
            return Response({'error': 'Invalid username or password.'}, status=401)

# UPDATE user accounts ----->
class UserProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer



# DELETE user accounts ----->
class UserProfileDelete(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
 


# FILTER user accounts ----->
class UserProfileFilter(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["username"]








