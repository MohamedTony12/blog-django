
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpeg',
                              upload_to='profile', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self,*args, **kwargs) -> None:
        super().save(*args, **kwargs)   
        img = Image.open(self.image.path) 
        if img.width > 300 or img.height > 300:
            img.thumbnail((300,400))
            img.save(self.image.path)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
