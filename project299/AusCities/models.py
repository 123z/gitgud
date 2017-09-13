from django.db import models


##class EnumField(models.Field):
##    """
##    A field class that maps to MySQL's ENUM type.
##    From - https://stackoverflow.com/a/1530858
##    Usage:
##
##    class Card(models.Model):
##        suit = EnumField(values=('Clubs', 'Diamonds', 'Spades', 'Hearts'))
##
##    c = Card()
##    c.suit = 'Clubs'
##    c.save()
##    """
##    def __init__(self, *args, **kwargs):
##        self.values = kwargs.pop('values')
##        kwargs['choices'] = [(v, v) for v in self.values]
##        kwargs['default'] = self.values[0]
##        super(EnumField, self).__init__(*args, **kwargs)
##
##    def db_type(self, connection):
##        return "enum({0})".format(','.join("'%s'" % v for v in self.values))

class EnumField(models.Field):
#From - https://stackoverflow.com/a/9633015
    
    def __init__(self, *args, **kwargs):
        super(EnumField, self).__init__(*args, **kwargs)
        if not self.choices:
            raise AttributeError('EnumField requires `choices` attribute.')

    def db_type(self, connection):
        return "enum(%s)" % ','.join("'%s'" % k for (k, _) in self.choices)
# Create your models here.



class UserType(models.Model):
    userType = models.CharField(max_length=20)
    def __str__(self):
        return self.userType
    
class User(models.Model):
    userType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    def __str__(self):
            return self.username

    
class User2(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    usertype = EnumField(choices=(('Student', 's'), ('Tourist', 't'), ('Businessman', 'b')))
    def __str__(self):
            return self.username