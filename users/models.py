from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

USER_TYPE = (
    ('Attendee', 'Attendee'),
    ('Organizer', 'Organizer'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(
        choices=USER_TYPE, max_length=10, default='Attendee', null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    idcard = models.ImageField(default='default.jpg', upload_to="idcard")
    idnumber = models.CharField(default="", max_length=50)
    numberofupdates = models.CharField(default='0', null=True, max_length=100)
    about = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Profile, self).save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
