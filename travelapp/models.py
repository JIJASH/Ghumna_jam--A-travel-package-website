from django.db import models
from django.contrib.auth.models import AbstractUser,Permission
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    contact_number=models.CharField(max_length=15,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True) 
    




class Customer(models.Model):
    
    first_name=models.CharField(max_length=50,blank=True,null=True)
    middle_name=models.CharField(max_length=50,blank=True,null=True)
    last_name=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    contact_number=models.CharField(max_length=20,blank=True,null=True)
    
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    
    GENDER_CHOICES=[
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHER'),
    ]
    
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True, null=True
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="customer")
    





class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField(default=dict, blank=True)  # Example: {"wifi": True, "pool": False}
    contact_number=models.CharField(max_length=20,blank=True,null=True)
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], blank=True, null=True
    )

    def __str__(self):
        return self.name






class TravelPackage(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available_from=models.DateField()
    available_to=models.DateField()
    location=models.CharField(max_length=255,blank=True,null=True)
    features = models.JSONField(default=dict)  
    hotels = models.ManyToManyField(Hotel, related_name='travel_packages', blank=True)
    
    def __str__(self):
        return self.name
    
    
    
    



class SeasonalPrice(models.Model):
    travel_package = models.ForeignKey(
        TravelPackage, on_delete=models.CASCADE, related_name="seasonal_prices"
    )
    season = models.CharField(max_length=50)  # e.g., "Winter", "Summer", "Christmas"
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.season} Price for {self.travel_package.name}"






class Booking(models.Model):
    
    STATUS_CHOICES=[
        ("Pending","Pending"),
        ("Confirmed","Confirmed"),
        ("Cancelled","Cnacelled"),
    ]
    PAYMENT_STATUS_CHOICES=[
        ("Unpaid","Unpaid"),
        ("Paid","Paid"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bookings")   
    travel_package=models.ForeignKey(TravelPackage, on_delete= models.CASCADE , related_name="bookings")
    booking_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Pending")
    payment_status=models.CharField(max_length=20,choices=PAYMENT_STATUS_CHOICES,default="Unpaid")
    travel_date=models.DateField()
    number_of_travelers=models.PositiveIntegerField(default=1)
   
    def get_applicable_price(self):

        seasonal_price = self.travel_package.seasonal_prices.filter(
            start_date__lte=self.travel_date, end_date__gte=self.travel_date
        ).first()

        return seasonal_price.price if seasonal_price else self.travel_package.price
    
    def __str__(self):
        return f"Booking by {self.customer.user.username}"







class Payment(models.Model):
    
    PAYMENT_METHOD_CHOICES=[
        ("ESEWA","ESEWA"),
        ("Khalti","Khalti"),
        ("Bank Transfer","Bank Transfer"),
        
    ]    
    PAYMENT_STATUS_CHOICES=[
        ("Pending","Pending"),
        ("Completed","Completed"),
        ("Failed","Failed"),
    ]
    booking=models.OneToOneField(Booking,on_delete=models.CASCADE,related_name="payment")
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_date=models.DateTimeField(auto_now_add=True)
    payment_method=models.CharField(max_length=20,choices=PAYMENT_METHOD_CHOICES)
    payment_status=models.CharField(max_length=20,choices=PAYMENT_STATUS_CHOICES,default="Pending")
    
    
    def __str__(self):
        return f"Payment for booking {self.booking.id}"
    
    
    
    
    
    
class Review(models.Model):
   
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="reviews")
    travel_package=models.ForeignKey(TravelPackage, on_delete= models.CASCADE , related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])   
    comment=models.TextField(blank=True,null=True)
    review_date=models.DateTimeField(auto_now_add=True)
    reply=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f"Review by {self.user.username} for {self.travel_package.name}"






class WishList(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="wishlist")
    travel_package=models.ForeignKey(TravelPackage, on_delete= models.CASCADE , related_name="wishlist")
    added_date=models.DateTimeField(auto_now_add=True)
    
    
    
    

    
    

   

    