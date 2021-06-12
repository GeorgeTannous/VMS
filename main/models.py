from django.db import models


def create_vacation(self, user_name, from_date_time, to_date_time, description):
    vac = self.model(user_name=user_name, from_date_time=from_date_time, to_date_time=to_date_time,
                     description=description)
    vac.save()
    return vac


class vacations(models.Model):
    user_name = models.CharField(max_length=100)
    from_date_time = models.CharField(max_length=30)
    to_date_time = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['user_name', 'from_date_time', 'to_date_time', 'description']
