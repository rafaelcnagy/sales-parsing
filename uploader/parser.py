import datetime
from uploader.models import Person, Product, Transaction
from textwrap import wrap


def parse_sales(file):
    def detach_transaction(line):
        return int(line[:1]), line[1:26], line[26:56].strip(), int(line[56:66]), line[66:].strip()
    
    file_content = file.read()
    
    for content_line in wrap(file_content.decode('utf-8'), 86):
        type, date_str, product_name, value, person_name = detach_transaction(content_line)

        date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        
        product, _ = Product.objects.get_or_create(name=product_name)
        person, _ = Person.objects.get_or_create(name=person_name)
       
        transaction = Transaction.objects.create(
            type=type,
            date=date,
            product=product,
            value=value,
            person=person
        )

        if type == 1:
            product.producers.add(person)
            person.balance += value
            product.save()
        elif type == 2:
            product.affiliates.add(person)
            person.balance += value
            product.save()
        elif type == 3:
            person.balance -= value
        elif type == 4:
            person.balance += value
        else:
            raise NotImplementedError()

        person.save()

