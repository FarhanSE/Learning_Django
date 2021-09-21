from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Profiles
from django.contrib.auth.models import User

# @receiver(post_save, sender=Profiles)
def profileCreated(sender, instance, created, **kwargs):
    user = instance
    profile = Profiles.objects.create(
        user= user,
        username = user.username,
        email = user.email,
        name = user.first_name
    )
post_save.connect(profileCreated, sender=User)

def profileUpdated(sender, instance, created, **kwargs):
    print("Instace:", instance)
    print("created:" , created)

post_save.connect(profileUpdated, sender=Profiles)


def profileDeleted(sender, instance,  **kwargs):
    user = instance.user
    user.delete()
    print("Instace: ", instance)
    print("Profile Deleting")

post_delete.connect(profileDeleted, sender=Profiles)
