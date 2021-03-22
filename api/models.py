from django.db import models

# Create your models here.

# Data Representation/Abstraction of a Team in the database

class Sled(models.Model):
    name = models.CharField(max_length=33)
    victories = models.IntegerField(default=0)
    defeats = models.IntegerField(default=0)

    # Special method that lets django know how a object should be primarily identified for representation purposes
    def __str__(self):
        return self.name

# Data Representation/Abstraction of a  in the database


class TeamMember(models.Model):

    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=12)

    sled = models.ForeignKey("Sled", null=True, on_delete=models.SET_NULL)
    captain = models.BooleanField(default=False, null=False)

    def full_name(self):
        return self.first_name + " " + self.last_name
