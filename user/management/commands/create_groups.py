from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create base groups'
    groups = {
    'Nutritionist': ['add_antopometric_evaluation', 'view_antopometric_evaluation', 'delete_add_antopometric_evaluation', 'change_antopometric_evaluation',

        
        'view_clinicevaluation','add_antopometricevaluation','change_antopometricevaluation','delete_antopometricevaluation','view_antopometricevaluation','add_clinicevaluation','change_clinicevaluation','delete_clinicevaluation','view_clinicevaluation', 'add_gastrointestinaltractsymptoms','change_gastrointestinaltractsymptoms',\
	'delete_gastrointestinaltractsymptoms','view_gastrointestinaltractsymptoms','add_labexam','change_labexam','delete_labexam','view_labexam','add_dietplan','change_dietplan','delete_dietplan','view_dietplan', 'view_exercisetype','add_exercise', 'change_exercise', 'delete_exercise', 'view_exercise', 'add_exercisetype', 'change_exercisetype',\
	'delete_exercisetype', 'view_exercisetype', 'delete_foodconsumption', 'view_foodconsumption', 'add_foodintolerance', 'change_foodintolerance', 'delete_foodintolerance', 'view_foodintolerance','add_foodpreferences', 'change_foodpreferences', 'delete_foodpreferences', 'view_foodpreferences', 'add_fooddiary','change_fooddiary', 'delete_fooddiary',\
	'view_fooddiary', 'add_familyhealthhistory', 'change_familyhealthhistory', 'delete_familyhealthhistory', 'view_familyhealthhistory', 'add_patienthealthhistory','change_patienthealthhistory', 'delete_patienthealthhistory', 'view_patienthealthhistory', 'add_nutritionalconduct', 'change_nutritionalconduct', 'delete_nutritionalconduct', 'view_nutritionalconduct','view_patient','view_phone'],
    'Receptionist': ['add_patient', 'change_patient', 'view_patient', 'add_phone', 'change_phone','delete_phone', 'view_phone', 'add_state', 'change_state','view_state','view_nutritionalconduct','view_labexam','add_dietplan', 'add_city', 'change_city'],
    'Administrator':[ 'add_antopometricevaluation','change_antopometricevaluation', 'delete_antopometricevaluation', 'view_antopometricevaluation', 'add_clinicevaluation', 'change_clinicevaluation', 'delete_clinicevaluation', 'view_clinicevaluation',\
    'view_clinicevaluation', 'add_gastrointestinaltractsymptoms', 'change_gastrointestinaltractsymptoms', 'delete_gastrointestinaltractsymptoms','view_gastrointestinaltractsymptoms', 'add_labexam',\
    'change_labexam', 'delete_labexam', 'view_labexam', 'add_dietplan', 'change_dietplan', 'delete_dietplan', 'view_dietplan', 'add_employee', 'change_employee', 'delete_employee', 'view_employee',\
    'add_exercisetype', 'change_exercisetype', 'delete_exercisetype', 'view_exercisetype', 'add_exercise', 'change_exercise', 'delete_exercise', 'view_exercise', 'add_foodconsumption',\
    'change_foodconsumption', 'delete_foodconsumption', 'view_foodconsumption', 'add_foodintolerance','change_foodintolerance', 'delete_foodintolerance', 'view_foodintolerance','add_foodpreferences',\
    'change_foodpreferences', 'delete_foodpreferences', 'view_foodpreferences', 'add_fooddiary','change_fooddiary', 'change_fooddiary', 'change_fooddiary', 'delete_fooddiary', 'view_fooddiary',\
    'add_foodgroup', 'change_foodgroup', 'delete_foodgroup', 'view_foodgroup', 'add_food', 'change_food','delete_food', 'view_food', 'add_familyhealthhistory', 'change_familyhealthhistory', 'delete_familyhealthhistory',\
    'view_familyhealthhistory', 'add_patienthealthhistory', 'change_patienthealthhistory', 'delete_patienthealthhistory', 'view_patienthealthhistory', 'add_state', 'change_state', 'delete_state', 'view_state',\
    'add_city', 'change_city', 'delete_city', 'view_city', 'add_patient', 'change_patient', 'delete_patient', 'view_patient', 'add_phone','change_phone', 'delete_phone', 'view_phone', 'add_nutritionalconduct',\
    'change_nutritionalconduct', 'delete_nutritionalconduct', 'view_nutritionalconduct', 'add_user', 'change_user', 'delete_user', 'view_user'],
    }
    def handle(self, *args, **kwargs):
        for groupName in self.groups:
            new_group, created = Group.objects.get_or_create(name=groupName)
            for permission in self.groups[groupName]:
                proj_add_perm = Permission.objects.get(codename=permission)
                new_group.permissions.add(proj_add_perm)