 from ques import models
 from rest_framework import serializers

 class QuestionSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.Question
         fields = ('id','questioner','text')

 class WordSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.Word
         fields = ('id','text')

 class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = models.User
         fields = ('id','name','username')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Response
        fields = ('id','question','user','word','timestamp','rank')
