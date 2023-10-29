from django.db import models
from .models import Customer, Tag, Product, Order



class ParentModel(models.Model):
    name = models.CharField(max_length=20, null=True)

class ChildModel(models.Model):
    name = models.CharField(max_length=20, null=True)
    parent = models.ForeignKey(ParentModel, null=True)


parent = ParentModel.objects.first()
# it will return all the child data related to parent.
child = parent.childmodel_set.all() # Here we need to take child model name in 'lowercase' then set as 'child_set'




# **************************************************  CREATE QUERIES HERE ***************************************************


# 1. Returns all Traveler
customers = Customer.objects.all()


# 2. Returns first Traveler in table
customer1 = Customer.objects.first() # it will return the traveler which was first created not new one which was last created

# we can also get first Customer from above queryset customers
customer1 = print(customers.first())

# 3. Returns last Traveler in table
customer1 = Customer.objects.last() # it will return the traveler which was created in the last not old traveler which was first created


# 4. Returns single traveler by name
customer1 = Customer.objects.get(name='Raju')
customer1.email
customer1.id


# 5. Returns single traveler by id
traveler = Customer.objects.get(id=1)  # Raju rastogi. Now we can get any field like traveler.email, traveler.phone



# 6. Returns all bookings related to customer (first customer)
# It will work with get(), first(), last() but not work with all(), filter() cuz these return QuerySet object

customer1 = Customer.objects.get(id=1)  # first() will return the single object
orders = customer1.order_set.all() # because traveler is connected to booking table with ForeignKey


# Or we can also use select_related()
# traveler_bookings = Booking.objects.filter(traveler__first_name='Raju').select_related('trip')


# # 7. Returns Booking's traveler name
# booking = Booking.objects.first()
# booking.traveler.first_name


# # Or we can also use select_related()
# traveler_name = Booking.objects.select_related('traveler', 'trip').values('trip__trip_name', 'traveler__first_name')
# print(traveler_name)

# """
# O/p : <QuerySet [{'trip__trip_name': 'Shimla Trek', 'traveler__first_name': 'Raju'}, 
#         {'trip__trip_name': 'Manali Trek', 'traveler__first_name': 'Raju'}, 
#         {'trip__trip_name': 'Shimla Trek', 'traveler__first_name': 'Karishma'}]>

# """


# # 8. Returns trips from Trip table with value
# trip = Trip.objects.filter(trip_name='Shimla Trek')
# print(trip) # if trip_name is not matching then will return empty queryset (None) - <QuerySet []>


# # 9. Order Objects/Sort Objects by id
# booking = Booking.objects.all().order_by('id')
# print(booking) # least to greatest(first inserted object to last inserted object)


# # 10. Order Objects/Sort Objects by id
# booking = Booking.objects.all().order_by('-id')
# print(booking) # greatest to least(last inserted object to first inserted object)


# # 11. Order Objects/Sort Objects by id
# booking = Booking.objects.all().order_by('-id')
# print(booking) # greatest to least(last inserted object to first inserted object)


