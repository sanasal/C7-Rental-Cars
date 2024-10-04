from datetime import date
from django.db.models import Q

def delete_expired_drop_offs(model):
    today = date.today()
    model.objects.filter(drop_off_date__lt=today).delete()