from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet, CharFilter, DateTimeFilter
from django_filters.widgets import RangeWidget

from .models import Project, ToDo


class ProjectFilter(FilterSet):
    name = CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class ToDoFilter(FilterSet):
    project = CharFilter(lookup_expr='contains')
    create_date = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        model = ToDo
        fields = ['project', 'create_date']
