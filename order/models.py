from django.db import models

from customer.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=True)

    def __str__(self):
        return self.robot_serial


