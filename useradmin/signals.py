from django.dispatch import receiver
from staff.models import staffmodel
from student.models import examsmodel
from .views import my_signal
from django.db.models.signals import post_save, pre_delete, m2m_changed, pre_save, post_delete, pre_init, post_init, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.test.signals import setting_changed, template_rendered


@receiver(post_save ,sender = staffmodel)
def staffgot(sender, instance, created, **kwargs):
    print("data in post save was  ","Sender:",sender,"Instance:", instance,"Created:", created,"Kwargs:", kwargs )
    print("new staff added")

@receiver(pre_delete, sender= staffmodel)
def stafftogo(sender, instance, using, origin, **kwargs):
    print("to be deleted, ","Sender:",sender,"Instance:", instance,"Using:", using, "Origin:", origin , "kwargs:", kwargs)

@receiver(m2m_changed, sender = examsmodel.studentforexam.through)
def studentsforexam(sender, instance, action , **kwargs):
    print("data is , sender", sender,'Instance:', instance, 'Action:', action, 'kwargs:', kwargs)
    print("ids included in pk set are ",kwargs['pk_set'])

@receiver(pre_save, sender = staffmodel)
def staffready(sender, instance, **kwargs):
    print("pre save kwargs are ", kwargs)
    

@receiver(post_delete, sender = staffmodel)
def staffleft(**kwargs):
    print("Data in post delete: ", kwargs)


@receiver(my_signal)
def customsignal(sender, **kwargs):
    print(kwargs)


@receiver(pre_init, sender = staffmodel)
def staffmodelinit(sender, **kwargs):
    print("staffmodel initializing", kwargs)


@receiver(post_init, sender = staffmodel)
def staffmodelready(sender, **kwargs):
    print("staff model initialised successfully", kwargs)


@receiver(pre_migrate)
def migpre(**kwargs):
    print("premig kwargs are ", kwargs)

@receiver(post_migrate)
def migpost(**kwargs):
    print("post mig kwargs are", kwargs)


# @receiver(request_started)
# def serverrequested(**kwargs):
#     print("Http request kwargs are ", kwargs)

# @receiver(request_finished)
# def serverrequested(**kwargs):
#     print("\nHttp FINISHED request kwargs are ", kwargs)

@receiver(got_request_exception)
def exc(**kwargs):
    print("\n\n\n HTTP Exception got :", kwargs)

@receiver(template_rendered)
def ttest(**kwargs):
    print("Template has been rendered", kwargs)