from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    contact = models.IntegerField(null=True)
    salary = models.IntegerField(blank=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Employee'