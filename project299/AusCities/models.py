from django.db import models

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
    
class Admin(models.Model):
    adminid = models.AutoField(db_column='adminID', primary_key=True)
    emailaddress = models.EmailField(db_column='emailAddress', max_length=80, blank=False, null=True)
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)
    password = models.CharField(db_column='password', max_length=350, blank=True, null=True)
    class Meta:
        db_table = 'admin'
    
class User(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    emailaddress = models.EmailField(db_column='emailAddress', max_length=80, blank=False, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usertype = EnumField(choices=(('Student', 'Student'), ('Tourist', 'Tourist'), ('Businessman', 'Businessman')), default = 1)
    password = models.CharField(max_length=400, blank=True, null=True)
    class Meta:
        #managed = False
        db_table = 'user'


class Location(models.Model):
    locationid = models.AutoField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='emailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    locationtype = models.CharField(db_column='locationType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'
        
class Collegedepartments(models.Model):
    locationdepartmentid = models.ForeignKey('Location', models.DO_NOTHING, db_column='locationDepartmentID')  # Field name made lowercase.
    department = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collegedepartments'

class Industrytypes(models.Model):
    locationindustryid = models.ForeignKey('Location', models.DO_NOTHING, db_column='locationIndustryID')  # Field name made lowercase.
    industrytype = models.CharField(db_column='industryType', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'industrytypes'
