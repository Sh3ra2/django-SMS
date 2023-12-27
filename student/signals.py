from django.apps import AppConfig
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from .models import examsmodel, subjectpapermodel

# @receiver(m2m_changed, sender =  examsmodel.studentforexam.through)
def handle_studenforexam_change(sender, instance, action, **kwargs):
    print("checking the students selected for exam, track db relation")
    if action == "post_add":
        create_subjectmodel_fromexam(instance)


@receiver(post_save, sender = examsmodel)
def handle_save(sender, instance, created, **kwargs):
    print("saving instance")
    if created:
        create_subjectmodel_fromexam(instance)


def create_subjectmodel_fromexam(examinstance):
    print("creating form for students")
    print("overall data is ", examinstance)
    
    print("data is ", examinstance.studentforexam.all())

    for student in examinstance.studentforexam.all():
        print("from for loop")

        subject_paper_instance = subjectpapermodel(
            exam= examinstance,
            esubject= examinstance.esubject,
            pstudent=student,
            total_marks=0,  # Set an initial value
            obtained_marks=0  # Set an initial value
        )
        try:
            subject_paper_instance.save()
        except Exception as e:
            print(f"Error saving subject paper model: {e}")

    print("Saving form")