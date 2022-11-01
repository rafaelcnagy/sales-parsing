from django.db import models

class Person(models.Model):
    """
    Stores seller data.

    @name [string]: name of seller
    @balance [int]: balance of seller
    """
    name = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField(default=0)

    def get_balance(self):
        """ Return person balance in float"""
        return self.balance/100.0

class Product(models.Model):
    """
    Stores product data and related people.

    @name [string]: name of product
    @producers [list(Person)]: list of producters of this product 
    @affiliates [list(Person)]: list of affiliates of this product 
    """
    name = models.CharField(max_length=30, unique=True)
    producers = models.ManyToManyField(Person, related_name='producers')
    affiliates = models.ManyToManyField(Person, related_name='affiliate')

class Transaction(models.Model):
    """
    Stores transaction data with all inputted data

    @type [int]: transaction type
    @person [Person]: person associated with transaction
    @date [datetime]: date of transaction
    @product [Product]: product associated with transaction
    @value [int]: value of transaction in cents 
    """

    type = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.IntegerField()

    def get_value(self):
        """ Return transaction value in float"""
        return self.value/100.0