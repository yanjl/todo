from django.db import models


# Create your models here.
class DoModel(models.Model):
    """Model definition for DoModel."""

    # TODO: Define fields here
    name = models.CharField(max_length=300, verbose_name='name')

    class Meta:
        """Meta definition for DoModel."""

        verbose_name = 'DoModel'
        verbose_name_plural = 'DoModels'

    def __str__(self):
        """Unicode representation of DoModel."""
        return self.name

    # def save(self):
    #     """Save method for DoModel."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for DoModel."""
    #     return ('')

    # TODO: Define custom methods here
