from django.views.generic import ListView

from .models import ComplaintCategory
from .models import Complaint

class HomeView(ListView):
    template_name = "home.html"
    model = Complaint
    
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('complaint_category')

