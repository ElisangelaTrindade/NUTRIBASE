
from django.views.generic import View
from diet_plan.models import DietPlan
from meal.models import Meal
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .render import Render


class Pdf(View):
    def get(self, request, diet_plan_id):
        date_of_consultation = timezone.now()
        bmi = ""
        diet_plan = DietPlan.objects.get(pk=diet_plan_id)
        meals = Meal.objects.filter(object_id = diet_plan.id, content_type_id = ContentType.objects.get_for_model(diet_plan).id)

        # Sanity check, we cannot have more than one
        if diet_plan.nutritionalconduct_set.all().count() is 1:
            conduct = diet_plan.nutritionalconduct_set.first()
            bmi = conduct.stringify_bmi()
            if conduct.antopometric_evaluation is not None:
                #By design we can only have one assigned here due to the dependency on the nutritional conduct
                date_of_consultation = diet_plan.nutritionalconduct_set.first() \
                    .antopometric_evaluation.date_of_consultation

        params = {
            'diet_plan': diet_plan,
            'meals': meals,
            'bmi': bmi,
            'date_of_consultation': date_of_consultation,
        }

        return Render.render('pdf.html', params)