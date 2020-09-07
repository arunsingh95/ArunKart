from django.core.exceptions import ObjectDoesNotExist
from django.http import QueryDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from test_api_orm.serializers import UserDetailSerializer, TaskPostSerializer, ProjectContentPostSerializer
from test_api_orm.models import UserDetails
from rest_framework.permissions import IsAuthenticated
from test_api_orm.permissions import IsAllowedToWrite #, IsOwnerOrReadOnly ,#IsAllowedToWrite #, IsAllowedToWrite
from test_api_orm.models import ProjectContent, Task


class UserDetailApi(APIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAllowedToWrite,)

    def get(self, request, user_id=None):
        # print(user_id)
        if user_id:
            model = UserDetails.objects.get(id=user_id)
            serializer = UserDetailSerializer(model)
        else:
            model = UserDetails.objects.all()
            print(model.values('is_married'))
            serializer = UserDetailSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        try:
            model = UserDetails.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserDetailSerializer(model, data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskApi(APIView):
    def get(self, request):
        serializer = UserDetailSerializer(many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        CSV Import - Task and Project Content Post Api
        :param request:
        :return:
        """
        serializer = ''
        error_dict = {}
        for i, j in request.data.items():
            query_dict = QueryDict('', mutable=True)
            for k in list(dict(self.request.query_params).values())[0]:
                if k in ['project', 'search_type']:
                    if j['id']:
                        query_dict.update(j)
                        model = ProjectContent.objects.get(id=j['id'])
                        serializer = ProjectContentPostSerializer(model, data=query_dict)
                    if not j['id']:
                        query_dict.update({key: val for key, val in j.items() if val is not ''})
                        serializer = ProjectContentPostSerializer(data=query_dict)
                if k in ['project_content', 'task']:
                    if j['id']:
                        query_dict.update(j)
                        model = Task.objects.get(id=j['id'])
                        serializer = TaskPostSerializer(model, data=query_dict)
                    if not j['id']:
                        query_dict.update({key: val for key, val in j.items() if val is not ''})
                        serializer = TaskPostSerializer(data=query_dict)
            if serializer.is_valid():
                serializer.save()
            else:
                error_dict[i] = serializer.errors
        return Response(error_dict, status=status.HTTP_200_OK)


