from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from media_app.tasks import send_mail_func
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# GET posts 
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

# CREATE posts 
class PostCreate(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

# GET user accounts 
class UserProfileList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

# CREATE user accounts 
class UserProfileCreate(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

# LOGIN 
class UserProfileLogin(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        # Check if the user exists and their password is correct.
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid username or password.'}, status=401)
        else:
            send_mail_func.delay()
            return Response({'message': 'Login successful.'}, status=200)

# UPDATE user accounts 
class UserProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

# DELETE user accounts 
class UserProfileDelete(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    

# FILTER user accounts 
class UserProfileFilter(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["username"]
    
# Caching
@method_decorator(cache_page(60*60))
def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)


