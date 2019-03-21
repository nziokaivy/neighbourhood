from django.db import models
from django.contrib.auth.models import User


class Neighbourhood(models.Model):
    CITY_CHOICES = (
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Mombasa', 'Mombasa'),
        ('Machakos', 'Machakos'),
        ('Kisumu', 'Kisumu'),
        ('Eldoret', 'Eldoret'),
        ('Malindi', 'Malindi'),
        ('Diani', 'Diani'),
        ('Naivasha', 'Naivasha'),
        ('Kiambu', 'Kiambu'),

    )

    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(choices=CITY_CHOICES, max_length=200 ,default=0, null=True, blank=True)
    neighbourhood_count= models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return self.neighbourhood_name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.filter(pk=id)
        neighbourhoods.delete()

    @classmethod
    def get_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.get(pk=id)
        return neighbourhoods

    @classmethod
    def filter_by_location(cls, location):
        neighbourhoods = cls.objects.filter(location=location)
        return neighbourhoods

    @classmethod
    def search_neighbourhood(cls, search_term):
        neighbourhoods = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return neighbourhoods

    @classmethod
    def update_neighbourhood(cls, id):
        neighbourhoods = cls.objects.filter(id=id).update(id=id)
        return neighbourhoods

class Profile(models.Model):
    profile_photo = models.ImageField( upload_to = 'profiles/', null=True)
    user_bio = models.CharField(max_length = 100, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
     
    
    def save_profile(self):
        self.save() 

    def get_absolute_url(self): 
        return reverse('user_profile')  

     

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile    

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile 
    
    def __str__(self):
        return f'{self.user.username} Profile'



class Business(models.Model):
    business_name = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="business")
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,related_name="neighbourhoodbusiness",null=True,blank=True)
    business_email_address = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.business_name


    def save_business(self):
        self.save()

    @classmethod
    def delete_business_by_id(cls, id):
        businesses = cls.objects.filter(pk=id)
        businesses.delete()

    @classmethod
    def get_businesses_by_id(cls, id):
        businesses = cls.objects.get(pk=id)
        return businesses

    @classmethod
    def filter_by_location(cls, location):
        businesses = cls.objects.filter(location=location)
        return businesses

    @classmethod
    def search_businesses(cls, search_term):
        businesses = cls.objects.filter(business_name__icontains=search_term)
        return businesses

    @classmethod
    def update_business(cls, id):
        businesses = cls.objects.filter(id=id).update(id=id)
        return businesses

    @classmethod
    def update_business(cls, id):
        businesses = cls.objects.filter(id=id).update(id=id)
        return businesses