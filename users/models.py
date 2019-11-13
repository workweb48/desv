from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='images')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    description = models.CharField(max_length=50,blank=True,null=True)
    cv_img_url = models.URLField(max_length=250)
    active = models.BooleanField(default=True)
    # key=models.CharField(max_length=10)
    def __str__(self):
        return '{} profile.'.format(self.user.username)



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])


post_save.connect(create_profile, sender=User)
