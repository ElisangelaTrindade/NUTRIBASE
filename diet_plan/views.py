
from django.views.generic import View
from diet_plan.models import DietPlan
from meal.models import Meal
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .render import Render


class Pdf(View):
    def get(self, request, diet_plan_id):
        evaluation = None
        conduct = None
        diet_plan = DietPlan.objects.get(pk=diet_plan_id)
        meals = Meal.objects.filter(object_id = diet_plan.id, content_type_id = ContentType.objects.get_for_model(diet_plan).id)

        if diet_plan.nutritionalconduct_set.all().count() is not 0:
            conduct = diet_plan.nutritionalconduct_set.first()
            if conduct.antopometric_evaluation is not None:
                #By design we can only have one assigned here due to the dependency on the nutritional conduct
                evaluation = diet_plan.nutritionalconduct_set.first() \
                    .antopometric_evaluation

        today = timezone.now()
        params = {
            'diet_plan': diet_plan,
            'meals': meals,
            'conduct': conduct,
            'evaluation': evaluation,
            'today': today
        }

        return Render.render('pdf.html', params)