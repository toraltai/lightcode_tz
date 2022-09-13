from rest_framework import viewsets, decorators, response
from rest_framework.response import Response
from .models import Students
from .serializers import StudentsSerializer
from django.db.models import Min,Max, Q, Count
from rest_framework.pagination import PageNumberPagination


class StudentsListView(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    pagination_class = PageNumberPagination
    
    @decorators.action(['GET'], detail=False)
    def max_and_min(self, request):
        max_age = Students.objects.aggregate(Max('age'))['age__max']
        min_age = Students.objects.aggregate(Min('age'))['age__min']
        res = Students.objects.filter(Q(age=max_age)|Q(age=min_age))
        return Response(StudentsSerializer(res, many=True).data)

    @decorators.action(detail=False)
    def count_list(self, request):

        res = Students.objects.all().count()
        context = {"count":res}
        return Response(context)