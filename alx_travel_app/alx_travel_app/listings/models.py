from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.


class listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Placeholder for user field
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.user}"


class Review(models.Model):
    listing = models.ForeignKey(listing, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Placeholder for user field
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.listing.title} by {self.user}"
