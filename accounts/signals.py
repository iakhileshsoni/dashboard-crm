from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer') # because we have 2 types of users for now that's why manually registering customer
        instance.groups.add(group)

        Customer.objects.create(user=instance, name=instance.username,)
        # print("Profile is created")

post_save.connect(customer_profile, sender=User)

"""
If I actually created another user from the admin panel then I wouldn't have to rewrite that logic in because I have signals listening to that
so that the senders and receivers are communicating and that's the beauty of using Signals in Django.
"""