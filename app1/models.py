from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    #age = models.IntegerField()
    gender = models.CharField(max_length=10)
    disease_effect = models.TextField()
    symptoms = models.TextField()
    precautions = models.TextField()
    course_duration=models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name