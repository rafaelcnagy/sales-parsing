from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    producers = models.ManyToManyField(Person, related_name='producers')
    affiliates = models.ManyToManyField(Person, related_name='affiliate')

class Transaction(models.Model):
    type = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.IntegerField()

    def get_value(self):
        return self.value/100