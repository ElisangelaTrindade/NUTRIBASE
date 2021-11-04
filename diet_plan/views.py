
from django.views.generic import View
from diet_plan.models import DietPlan
from meal.models import Meal
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .render import Render


class Pdf(View):
    def get(self, request, diet_plan_id):
        diet_plan = DietPlan.objects.get(pk=diet_plan_id)
        meals = Meal.objects.filter(object_id = diet_plan.id, content_type_id = ContentType.objects.get_for_model(diet_plan).id)
        evaluation = diet_plan.patient.antopometricevaluation_set.latest('date_of_consultation')

        #breakpoint()
        today = timezone.now()
        params = {
            'diet_plan': diet_plan,
            'meals': meals,
            'evaluation': evaluation,
            'today': today
        }

        return Render.render('pdf.html', params)