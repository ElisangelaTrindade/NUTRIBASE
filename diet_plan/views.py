
from django.views.generic import View
from diet_plan.models import DietPlan
from django.utils import timezone
from .render import Render


class Pdf(View):
    def get(self, request, diet_plan_id):
        diet_plan = DietPlan.objects.get(pk=diet_plan_id)
        today = timezone.now()
        params = {
            'diet_plan': diet_plan,
            'today': today
        }

        return Render.render('pdf.html', params)