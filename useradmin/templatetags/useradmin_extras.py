from django import template
from staff.models import staffmodel
from student.models import studentmodel
from django.db.models import Count

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
    return gender_c