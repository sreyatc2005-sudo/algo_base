from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from repository.models import Questions
from repository.models import Submission

from repository.serializers import QuestionSerializer
from repository.serializers import SubmissionSerializer
from repository.serializers import SubmissionEvaluateSerializer

class QuestionsListCreateView(APIView):
    def get(self,request):
        qs=Questions.objects.all()
        serializer_instance = QuestionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance=QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Questions.objects.create(**cleaned_data)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk):
        qs=Questions.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Questions.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):

        deleted_data= Questions.objects.filter(id=pk).delete()
        return Response(data=deleted_data)
    
class SubmissionListCreateView(APIView):
    def get(self,request):
        qs=Submission.objects.all()
        serializer_instance=SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Submission.objects.create(**cleaned_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class SubmissionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(Submission,id=pk)
        serializer_instance=SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
            form_data=request.data
            serializer_instance=SubmissionSerializer(data=form_data)
            if serializer_instance.is_valid():
                cleaned_data=serializer_instance.validated_data
                Submission.objects.filter(id=pk).update(**cleaned_data)
                return Response(data=serializer_instance.data)
            else:
                return Response(data=serializer_instance.errors)

class EvaluateSubmissionView(APIView):
    def put(self,request,pk):
        form_data=request.data
        serializer_instance=SubmissionEvaluateSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            Submission.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)



    