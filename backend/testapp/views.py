from django.shortcuts import render, HttpResponse
from .models import Subject, Units, ImpQuestion

# Create your views here.

def home_view(request):
    return render(request, template_name='index.html')


def topper_view(request):
    return render(request, template_name='topper.html')


def coding_view(request):
    all_coding_subjects = Subject.objects.filter(sub_type = 'CODING')
    print(all_coding_subjects)
    return render(request, template_name='coding.html', context={'all_coding_subjects' : all_coding_subjects})


def theory_view(request):
    all_theory_subjects = Subject.objects.filter(sub_type = 'THEORY')
    print(all_theory_subjects)
    return render(request, template_name='theory.html', context={'all_theory_subjects' : all_theory_subjects})


def timer_view(request):
    return render(request, template_name='timer.html')

def sub_detail(request, sub):
    given_subject = Subject.objects.get(sub_name = sub)
    # print(given_subject)
    # print(given_subject.id)

    all_units_of_given_subject = Units.objects.filter(belongs_to = given_subject.id)
    imp_questions = ImpQuestion.objects.filter(subject_name = given_subject.id).first()
    print(imp_questions)
    print(imp_questions.question_file)

    # print(all_units_of_given_subject)

    return render(request, template_name='particular.html', context={'sub_name': sub,'all_units_of_given_subject' : all_units_of_given_subject, 'imp_questions' : imp_questions})
