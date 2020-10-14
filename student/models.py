from django.db import models

# Create your models here.
class Information(models.Model):
    number = models.CharField(max_length=9, null=False)
    name = models.CharField(max_length=20, null=False)
    domb = models.CharField(max_length=2, null=False)
    domr = models.CharField(max_length=3, null=False)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        fJSON = {}
        for attr in fields:
            fJSON[attr] = getattr(self, attr)

        return fJSON

