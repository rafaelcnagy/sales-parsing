import datetime
from django.test import TestCase
from django.utils import timezone
from uploader.models import Person, Product, Transaction

# Create your tests here.

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="Chaves")

    def test_person(self):
        """Person is created"""
        person = Person.objects.get(name="Chaves")
        self.assertEqual(person.name, "Chaves")
        self.assertEqual(person.get_balance(), 0)

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Telecurso 2001")

    def test_product(self):
        """Product without People is created correctly"""
        product = Product.objects.get(name="Telecurso 2001")
        self.assertEqual(product.producers.count(), 0)
        self.assertEqual(product.affiliates.count(), 0)

class ProductWithPersonsTestCase(TestCase):
    def setUp(self):
        product = Product.objects.create(name="Telecurso 2000")
        person1 = Person.objects.create(name="Chaves")
        person2 = Person.objects.create(name="Chiquinha")
        person3 = Person.objects.create(name="Seu Madruga")
        product.producers.add(person1)
        product.affiliates.add(person2)
        product.affiliates.add(person3)


    def test_product_producers(self):
        """Product with producers is created correctly"""
        product = Product.objects.get(name="Telecurso 2000")
        person = Person.objects.get(name="Chaves")
        self.assertEqual(list(product.producers.all()), [person])

    def test_product_affiliates(self):
        """Product with affiliates is created correctly"""
        product = Product.objects.get(name="Telecurso 2000")
        person1 = Person.objects.get(name="Chiquinha")
        person2 = Person.objects.get(name="Seu Madruga")
        self.assertEqual(list(product.affiliates.all()), [person1, person2])


class TransactionTestCase(TestCase):
    def setUp(self):
        product = Product.objects.create(name="Telecurso 2000")
        Transaction.objects.create(
            type=1,
            product=product,
            person=Person.objects.create(name="Chaves"),
            date=datetime.datetime.now(tz=timezone.utc),
            value=100000,
        )

    def test_transaction(self):
        """Transaction is created correctly"""
        person = Person.objects.get(name="Chaves")
        transaction = Transaction.objects.get(person=person)

        self.assertEqual(transaction.type, 1)
        self.assertEqual(transaction.person.name, 'Chaves')
        self.assertEqual(transaction.product.name, 'Telecurso 2000')
        self.assertEqual(transaction.get_value(), 1000)


class FileFormTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="Chaves")

    def test_person(self):
        """Person is created"""
        person = Person.objects.get(name="Chaves")
        self.assertEqual(person.name, "Chaves")
        self.assertEqual(person.get_balance(), 0)