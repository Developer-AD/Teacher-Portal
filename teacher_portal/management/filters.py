import django_filters
from .models import Student
from django.db.models import Q


class StudentFilter(django_filters.FilterSet):
    MARK_CHOICES = (
        ('high', 'High Marks (80+)'),
        ('medium', 'Medium Marks (60-79)'),
        ('low', 'Low Marks (Below 60)'),
    )
    
    search = django_filters.CharFilter(method='filter_by_search', label='Search')
    subject = django_filters.CharFilter(field_name='subject',lookup_expr='exact')
    marks_range = django_filters.ChoiceFilter(label='Marks Range', choices=MARK_CHOICES, method='filter_by_marks')
    
    class Meta:
        model = Student
        fields = ['search', 'subject', 'mark', 'marks_range']

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(subject__icontains=value)
        )

    def filter_by_marks(self, queryset, name, value):
        if value == 'high':
            return queryset.filter(mark__gte=80)
        elif value == 'medium':
            return queryset.filter(mark__gte=60, mark__lt=80)
        elif value == 'low':
            return queryset.filter(mark__lt=60)
        return queryset