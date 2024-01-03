from django import template
from staff.models import staffmodel
from student.models import studentmodel
from django.db.models import Count, Max, Case, When, Value, CharField, Min, Avg
from django.core.exceptions import ImproperlyConfigured
import sys

register = template.Library()

@register.simple_tag
def staff_count_by_joindate():
    # Your logic to get the count by admitted date
    count_by_date = staffmodel.objects.values('join_date').annotate(count=Count('id'))

    return count_by_date

@register.simple_tag
def staff_gender_count():
    gender_count = staffmodel.objects.values("gender").annotate(count = Count('id'))
    return gender_count


@register.simple_tag
def studentstats():
    gender_c = studentmodel.objects.values("gender").annotate(count = Count("id"))
    class_c = studentmodel.objects.values("sclass").annotate(count = Count("id"))
    admition_time = studentmodel.objects.values("date_time__date").annotate(count = Count("id"))
    print("gender count", gender_c)
    return gender_c


@register.simple_tag
def querytest():
    a = studentmodel.objects.filter(name__icontains = 'ba')
    b = studentmodel.objects.exclude(name__icontains = "thanos")
    print("a is ",a)
    return a,b

@register.simple_tag
def querytestano():
    # a = studentmodel.objects.annotate(big_class = Max('DOB'))
    a = studentmodel.objects.annotate(
        big_class=Case(
            When(DOB__year__lt=2000, then=Value('Not Gen')),
            default=Max('DOB'),
            output_field=CharField(),  # Adjust the output field type based on your needs
        )
    )
    b = studentmodel.objects.values('gender').annotate(count_g = Count("id"))
    c = studentmodel.objects.values('gender', 'admitted_by').annotate(count_m = Count("id")).order_by('-count_m')
    d = studentmodel.objects.values('sclass').annotate(max_age = Max('DOB')).annotate(min_age = Min('DOB'))
    print("annotate a is ",a,b,c)
    return a,b,c,d

@register.simple_tag
def querytesto():
    a = studentmodel.objects.values('name', 'gender').distinct()
    b = studentmodel.objects.filter(gender = 'M').values_list("id", flat = True)
    # c = studentmodel.objects.filter(gender = 'M').values('id')
    # print("\na is ", a,"\nb is ", b,"\nc is ",c)
    return a, b

@register.simple_tag
def queryven():
    a = studentmodel.objects.all()
    b = staffmodel.objects.all()
    c = a.union(b)
    d = a.intersection(b)
    e = a.difference(b)
    # print("c is ", c)
    return c, d, e

@register.simple_tag
def queryrelat():
    a = studentmodel.objects.select_related('admitted_by').all()
    print("select related is ", a)
    return a 

@register.filter
def filtertagcheck(value):
    return value.upper()

@register.filter
def addtwo(v1,v2):
    return v1+v2