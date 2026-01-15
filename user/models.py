from django.db import models

class User(models.Model):
    firstName = models.CharField('First Name', max_length=10, blank=True, null=True)
    lastName = models.CharField('Last Name', max_length=10, blank=True, null=True)
    maidenName = models.CharField('Maiden Name', max_length=10, blank=True, null=True)
    age = models.DecimalField('Age', max_digits=5, decimal_places=0, blank=True, null=True)
    gender = models.CharField('Gender', max_length=10, blank=True, null=True)
    email = models.CharField('Email', max_length=50, blank=True, null=True)
    phone = models.CharField('Phone', max_length=20, blank=True, null=True)
    username = models.CharField('User Name', max_length=10, blank=True, null=True)
    password = models.CharField('Password', max_length=10, blank=True, null=True)
    birthDate = models.DateField('Birth Date', max_length=15, blank=True, null=True)
    bloodGroup = models.CharField('Blood Group', max_length=5, blank=True, null=True)
    height = models.DecimalField('Height', max_digits=8, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField('Weight', max_digits=8, decimal_places=2, blank=True, null=True)
    eyeColor = models.CharField('Eye Color', max_length=10, blank=True, null=True)
    role = models.CharField('Role', max_length=10, blank=True, null=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName