 from ques.models import *
 from ques.serializers import *
 from rest_framework import viewsets

 class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer

 class QuestionViewSet(viewsets.ModelViewSet):
     queryset = Question.objects.all()
     serializer_class = QuestionSerializer

 class WordViewSet(viewsets.ModelViewSet):
     queryset = Word.objects.all()
     serializer_class = WordSerializer

 class ResponseViewSet(viewsets.ModelViewSet):
     queryset = Response.objects.all()
     serializer_class = ResponseSerializer
