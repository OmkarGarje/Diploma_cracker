from django.db import models

# Create your models here.

sub_type_choices = (
    ('CODING', 'Coding'),
    ('THEORY', 'Theory')
    )

class Subject(models.Model):
    sub_name    = models.CharField(max_length=150, unique=True)
    sub_type    = models.CharField(max_length=20, choices=sub_type_choices)
    sub_img     = models.ImageField(upload_to='images/')
    num_units   = models.IntegerField()


    def __str__(self):
        return self.sub_name



class Units(models.Model):
    unit_name   = models.CharField(max_length=250)
    unit_file   = models.FileField(upload_to="unit_files/")
    unit_number = models.IntegerField()
    belongs_to  = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.unit_name} | {self.belongs_to}"
    

    class Meta:
        verbose_name_plural = "Units"


class ImpQuestion(models.Model):
    subject_name    = models.OneToOneField(Subject, on_delete=models.CASCADE)
    question_file   = models.FileField(upload_to='imp_questions/')

    def __str__(self):
        return f'{self.subject_name} | Important Questions'
    
    