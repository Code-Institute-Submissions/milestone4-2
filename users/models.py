from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Extending the user profile by adding additional information.
        On delete argument CASCADE > when the user is deleted, his profile is deleted also,
        but if profile is deleted, user is not."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional information required for registration
    birthDate = models.DateField(blank=True, null=True)
    homeAddress = models.CharField(
        blank=True, max_length=200, default="Your home address"
    )
    phoneNumber = models.CharField(blank=True, max_length=20, default="0766 xxx xxx")
    profileImage = models.ImageField(default="default.jpg", upload_to="profile_images")

    def __str__(self):
        return f"{self.user.username} Profile"

    """Override save function in order to resize the image,
        so that the file system will not get loaded with big files,
        affecting performance."""

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     imgProfile = Image.open(self.profileImage.path)

    #     if imgProfile.height > 300 or imgProfile.width > 300:
    #         outputSize = (300, 300)
    #         imgProfile.thumbnail(outputSize)
    #         imgProfile.save(self.profileImage.path)

