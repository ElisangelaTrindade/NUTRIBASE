from django import forms
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_text
from django.forms.utils import flatatt
from food_group.models import Food

class MealSelectWidget(forms.Select):
  def __init__(self, attrs=None, choices=()):
      super(MealSelectWidget, self).__init__(attrs, choices)

  def render(self, name, value, attrs=None):
    self.choices = [(u"", u"" ,u"", u"---------")]
    for m in Food.objects.all():
      self.choices.append((m.calories, m.weight, m.id, smart_text(m)))

    final_attrs = self.build_attrs(attrs, {'name': name})
    output = ['<select%s>' % (flatatt(final_attrs))]
    for option in self.choices:
        isSelected = "selected" if option[2] == value else "" 
        output.append('<option calories="%s" base_weight="%s" value="%s" %s>%s</option>' % (option[0], option[1], option[2], isSelected, option[3]))
    output.append('</select>')
    return mark_safe(''.join(output))

