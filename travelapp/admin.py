from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','middle_name','last_name','address','contact_number','gender')
    search_fields=('first_name','contact_number',)
    list_filter=('gender',)
    list_per_page=10



@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display=('name','description','price','available_from','available_to','location','features',)
    list_filter=('name','price',)
    search_fields=('name','location','available_from',)
    list_per_page=10
    
    

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display=('travel_package','booking_date','status','payment_status','travel_date','number_of_travelers',)
    list_filter=('status','payment_status','number_of_travelers',)
    search_fields=('travel_package',)
    list_per_page=10



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=('booking','amount','payment_date','payment_method','payment_status',)
    search_fields=('booking',)
    



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('travel_package','rating','comment','review_date','reply',)
    search_fields=('travel_package',)
    list_filter=('rating',)
    list_editable=('reply',)





@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display=('travel_package','added_date',)
    search_fields=('travel_package',)
