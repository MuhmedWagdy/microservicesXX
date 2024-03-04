from django_filters import rest_framework as filters

from .models import Job




class JobFilter(filters.FilterSet):

    min_salary = filters.NumberFilter(field_name='salary',lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name='salary',lookup_expr='lte')
    keyword =  filters.CharFilter(field_name='title',lookup_expr='contains')
    date = filters.DateFilter(field_name='created_at',lookup_expr='range')

    class Meta:
        model = Job
        fields = ['keyword','job_type','education','experience','min_salary','max_salary','date']
