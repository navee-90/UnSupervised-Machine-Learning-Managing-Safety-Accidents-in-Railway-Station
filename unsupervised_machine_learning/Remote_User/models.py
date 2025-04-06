from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class accident_type_prediction(models.Model):

    RID= models.CharField(max_length=300)
    Location= models.CharField(max_length=300)
    Latitude= models.CharField(max_length=300)
    Longitude= models.CharField(max_length=300)
    Avgpassengersperday= models.CharField(max_length=300)
    Nooftrainspassing= models.CharField(max_length=300)
    Nooftrainsstopping= models.CharField(max_length=300)
    Noofplatforms= models.CharField(max_length=300)
    Nooftracks= models.CharField(max_length=300)
    Trainhaltingtime= models.CharField(max_length=300)
    Avgtrainspeed= models.CharField(max_length=300)
    Averageaccidentspermonth= models.CharField(max_length=300)
    population= models.CharField(max_length=300)
    PhysicalEnvironment= models.CharField(max_length=300)
    DateTime= models.CharField(max_length=300)
    admin_found= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



