from rest_framework import serializers

from repository.models import Questions

class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField()

    language = serializers.ChoiceField(choices=Questions.LANGUAGE_CHOICES)

    difficulty_level = serializers.ChoiceField(choices=Questions.DIFFICULTY_CHOICES)

    notes = serializers.CharField(read_only=True)

    topic = serializers.CharField()

    published_date = serializers.DateField(read_only=True)

    sample_input = serializers.CharField()

    sample_output = serializers.CharField()

    is_active =  serializers.BooleanField(read_only=True)

class SubmissionSerializer(serializers.Serializer):
    answer=serializers.CharField()

    question_id=serializers.IntegerField()

    points=serializers.IntegerField(read_only=True)

    owner=serializers.CharField()

    remarks=serializers.CharField(read_only=True)

    submission_date=serializers.DateTimeField(read_only=True)

    def validate(self, validated_data):
        question_id=validated_data.get("question_id")
        if not Questions.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("question not exist....") 
        return validated_data       

class SubmissionEvaluateSerializer(serializers.Serializer):
    points=serializers.IntegerField()
    remarks=serializers.CharField()
    def validate(self,validated_data):
        points=validated_data.get("points")
        if points>10 or points<0:
            raise serializers.ValidationError("invalid point..points should be in the range 1 to 19")


    
    
