from django.db import models

# Create your models here.
class Information(models.Model):
    number = models.CharField(max_length=9, null=False, unique=True)
    name = models.CharField(max_length=20, null=False)
    domb = models.CharField(null=True, blank=True, max_length=2, default=None)
    domr = models.CharField(null=True, blank=True, max_length=3, default=None)
    duty = models.CharField(null=True, blank=True, max_length=1, default=None)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        fJSON = {}
        for attr in fields:
            fJSON[attr] = getattr(self, attr)

        return fJSON

