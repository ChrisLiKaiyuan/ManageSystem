from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ManageSystem.utils import StandardResultsSetPagination
from .serializer import CreateInfoSerializer, GetInfoListSerializer, InfoSerializer, SearchInfoSerializer, \
    DutyInfoSerializer
from .models import Information


# Create your views here.
class CreateInfoView(CreateAPIView):
    serializer_class = CreateInfoSerializer
    queryset = Information.objects.all()

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


class SearchInfoView(GenericAPIView):
    serializer_class = SearchInfoSerializer
    queryset = Information.objects.all()

    def post(self, request):
        number = request.POST.get("number")
        name = request.POST.get("name")
        domb = request.POST.get("domb")
        domr = request.POST.get("domr")
        if number and name and domb and domr:
            data = Information.objects.filter(number=number, name=name, domb=domb, domr=domr)
            if data:
                students = Information.objects.filter(domb=domb, domr=domr).values()
                return Response(data=students)
            else:
                return Response(data={"Error": "信息错误或信息未完善！"})
        else:
            return Response(data={"Error": "请填写完整信息"})


def filt(dictionary):
    ret = []
    for d in dictionary:
        d = {"name": d["name"], "duty": d["duty"]}
        ret.append(d)
    return ret


class DutyInfoView(GenericAPIView):
    serializer_class = DutyInfoSerializer
    queryset = Information.objects.all()

    def post(self, request):
        domb = request.POST.get("domb")
        domr = request.POST.get("domr")
        duty = request.POST.get("duty")
        if domb and domr and duty:
            data = Information.objects.filter(domb=domb, domr=domr, duty=duty)
            if data:
                students = Information.objects.filter(domb=domb, domr=domr, duty=duty).values()
                students = filt(students)
                return Response(data=students)
            else:
                return Response(data={"Error": "信息错误或信息未完善！"})
        elif domb and domr:
            data = Information.objects.filter(domb=domb, domr=domr)
            if data:
                students = Information.objects.filter(domb=domb, domr=domr).values()
                students = filt(students)
                return Response(data=students)
            else:
                return Response(data={"Error": "信息错误或信息未完善！"})
        else:
            return Response(data={"Error": "请填写完整信息"})
