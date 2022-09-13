from rest_framework import viewsets, decorators, response
from rest_framework.response import Response
from .models import Students
from .serializers import StudentsSerializer
from django.db.models import Min,Max, Q

class StudentsListView(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()

    @decorators.action(['GET'], detail=False)
    def max_age(self, request):
        max_age = Students.objects.aggregate(Max('age'))['age__max']
        min_age = Students.objects.aggregate(Min('age'))['age__min']
        students = Students.objects.filter(Q(age=max_age)|Q(age=min_age))
        return Response(StudentsSerializer(students, many=True).data)