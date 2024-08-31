from django.db import models

class Customer(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth=models.DateField()
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10)

    def __str__(self):
        self.save()
        return (f"{self.first_name} {self.last_name}")

