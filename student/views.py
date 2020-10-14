from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from ManageSystem.utils import CustomException, ERROR_MESSAGE, StandardResultsSetPagination
from ManageSystem import settings
from .serializer import CreateInfoSerializer, GetInfoListSerializer, InfoSerializer
from .models import Information
from django.core.mail import send_mail
import requests
import json
import threading

# Create your views here.
class CreateInfoView(CreateAPIView):
    serializer_class = CreateInfoSerializer
    queryset = Information.objects.all()

    # 验证码
    def post(self, request, *args, **kwargs):
        number = request.data.get("number")
        print(number)
        try:
            data = Information.objects.get(number=number)
            print(data)
        except:
            return super(CreateInfoView, self).post(request, *args, **kwargs)
        else:
            print("{} Form Exists".format(number))
            return Response(data={"Form Exists"})


class GetInfoListView(ListAPIView):
    serializer_class = GetInfoListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Information.objects.all().order_by('id')
    pagination_class = StandardResultsSetPagination


class InfoView(RetrieveUpdateDestroyAPIView):
    serializer_class = InfoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Information.objects.all()

    def put(self, request, *args, **kwargs):
        return super(InfoView, self).put(request, *args, **kwargs)


class SearchInfoView(ListAPIView):
    serializer_class = InfoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Information.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('number', 'name', 'domb', 'domr')
