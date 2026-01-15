from django.db import models

class Employee(models.Model):
    first_name = models.CharField('First Name', max_length=10, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=10, blank=True, null=True)
    age = models.DecimalField('Age', max_digits=5, decimal_places=0, blank=True, null=True)
    monthly_salary = models.DecimalField('Monthly Salary', max_digits=10, decimal_places=2, blank=True, null=True)
    join_date = models.DateField('Join Date', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
