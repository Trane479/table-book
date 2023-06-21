from django.db import models

# Create your models here.


class RestaurantChain(models.Model):
    chain_name = models.CharField(max_length=256, primary_key=True)
    chain_id = models.IntegerField()


class RestaurantBranch(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    chain_name = models.ForeignKey(RestaurantChain, on_delete=models.CASCADE)
    contact_number = models.IntegerField()
    email = models.CharField()
    number_of_tables = models.IntegerField()
