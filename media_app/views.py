from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from media_app.tasks import send_mail_func
from django.utils.decorators import method_decorator

from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from rest_framework.permissions import BasePermission


# Permission class
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool( request.user and request.user.is_staff)

# GET posts ----->
class PostList(generics.ListAPIView):
    queryset=Post.objects.all().order_by('-created_on')
    serializer_class=PostSerializer
    permission_classes = [IsAdminUser] 
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
    permission_classes = [IsAdminUser] 

    


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

        # Check if the user exists and their password is correct.
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid username or password.'}, status=401)
        else:
            send_mail_func.delay()
            return Response({'message': 'Login successful.'}, status=200)


# UPDATE user accounts ----->
class UserProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [IsAdminUser] 


# DELETE user accounts ----->
class UserProfileDelete(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [IsAdminUser] 


# FILTER user accounts ----->
class UserProfileFilter(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["username"]

# Caching
@method_decorator(cache_page(60*60))
def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)










# @api_view(['GET','POST'])
# def posts(request):
#     # view the posts--->
#     if request.method=='GET':
#        posts = Post.objects.all()
#        serializer = PostSerializer(posts, many=True)
#        return Response(serializer.data)
#     # create posts--->
#     elif request.method=='POST':
#         serializer=PostSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET'])
# def post_list(request):
#     posts=Post.objects.all()
#     paginator = Paginator(posts, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     serializer=PostSerializer(page_obj,many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def filtering(request):
#     posts=Post.objects.all()
#     filter_backend=DjangoFilterBackend()
#     filter_field=['user']
#     filtered_posts=filter_backend(request,filter_field,posts)
#     return Response(filtered_posts.data)

    

