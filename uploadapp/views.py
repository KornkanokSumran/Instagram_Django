from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers

from .serializers import FileSerializer, DescriptionSerializer, CommentSerializer
from .models import File, Description, Comment

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
      
      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class count_like(APIView):    
    def post(self, request, *args, **kwargs):     
        temp = request.data
        name_id = temp.getlist("name_id")[0]
        try:
            print(name_id)
            name = Description.objects.get(name_id = name_id)
            print(name)
        except (KeyError, Description.DoesNotExist):
            name = Description(name_id = name_id)
            name.save()
        else:
            name.count += 1
            name.save()
        return Response({"File": "finish"})

class post_comment(APIView):    
    def post(self, request, *args, **kwargs):     
        temp = request.data
        name_id = temp.getlist("name_id")[0]
        comment = temp.getlist("comment")[0]
        print(temp)
        post = Comment(comment = comment, name_id = name_id)
        post.save()
        return Response({"File": "finish"})


class LikeView(APIView):
    def get(self, request):
        queryset = Description.objects.all()
        serializer = DescriptionSerializer(queryset, many=True)
        print(serializer.data)
        print(queryset)
        return Response({"File": serializer.data})

class CommentView(APIView):
    def get(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        print(serializer.data)
        print(queryset)
        return Response({"File": serializer.data})

class FileView(APIView):
    def get(self, request):
        queryset = File.objects.all()
        serializer = FileSerializer(queryset, many=True)
        print(serializer.data)
        print(queryset)
        return Response({"File": serializer.data})

# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = ('id', 'file')



