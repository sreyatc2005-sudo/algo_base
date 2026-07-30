from django.db import models

# Create your models here.

# scema:Questions
# fields: title,language,difficulty_level,notes,topics,published_date,sample_input,sample_output

class Questions(models.Model):
    title=models.CharField(max_length=200)
    LANGUAGE_CHOICES=(
        ("python","python"),
        ("java","java"),
        ("javascript","javascript"),
        ("c","c")
    )

    language=models.CharField(max_length=200,choices=LANGUAGE_CHOICES,default="python")
    DIFFICULTY_CHOICES=(
        ("easy","easy"),
        ("medium","medium"),
        ("hard","hard")
    )
    difficulty_level=models.CharField(max_length=200,choices=DIFFICULTY_CHOICES,default="easy")
    notes=models.TextField(null=True)
    topic=models.CharField(max_length=200)
    published_date=models.DateField(auto_now_add=True)
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_active=models.BooleanField(default=True)
    
