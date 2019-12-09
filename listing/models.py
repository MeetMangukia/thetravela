from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    room = models.IntegerField(verbose_name="Available Room")

    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    ac = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    mini_fridge = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    
    photo_main = models.ImageField(upload_to='photos/hotel/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/hotel/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/hotel/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/hotel/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    days = models.CharField(max_length=100)
    night = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    description = models.TextField(max_length=500)

    place_1_heading = models.CharField(max_length=100, blank=True)
    place_1 = models.TextField(max_length=500, blank=True)

    place_2_heading = models.CharField(max_length=100, blank=True)
    place_2 = models.TextField(max_length=500, blank=True)
    
    place_3_heading = models.CharField(max_length=100, blank=True)
    place_3 = models.TextField(max_length=500, blank=True)

    is_hot = models.BooleanField(verbose_name="Is Hot Deal", default=False)

    photo_main = models.ImageField(upload_to='photos/tour/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_11 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)
    photo_12 = models.ImageField(upload_to='photos/tour/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    members = models.CharField(max_length=100)
    bags = models.CharField(max_length=100)
    doors = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    photo_main = models.ImageField(upload_to='photos/car/%Y/%m/%d/')

    def __str__(self):
        return self.name