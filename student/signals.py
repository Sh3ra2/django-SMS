from django.apps import AppConfig
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import examsmodel, subjectpapermodel

@receiver(post_save, sender = examsmodel)
def create_subjectmodel_fromexam(sender, instance, created, **kwargs):
    print("creating form for students")
    print("overall data is ", kwargs)
    print("Instance actually is , ", instance)
    print("data is ", instance.studentforexam.all())

    for student in instance.studentforexam.all():
        print("from for loop")

        subject_paper_instance = subjectpapermodel(
            exam= instance,
            esubject= instance.esubject,
            pstudent=student,
            total_marks=0,  # Set an initial value
            obtained_marks=0  # Set an initial value
        )
        try:
            subject_paper_instance.save()
        except Exception as e:
            print(f"Error saving subject paper model: {e}")

    print("Saving form")