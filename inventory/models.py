from django.db import models

# Create your models here.
class ItemDetails(models.Model):
    item_id          =  models.CharField(max_length = 10)
    item_name        =  models.CharField(max_length = 50)
    description      =  models.CharField(max_length = 255)
    category         =  models.CharField(max_length = 10)
    barcode          =  models.CharField(max_length = 10)
    supplier         =  models.CharField(max_length = 10)
    min_stock        =  models.IntegerField(default = 0)
    max_stock        =  models.IntegerField(default = 0)
    cur_stock        =  models.IntegerField(default = 0)
    cost_price       =  models.DecimalField(decimal_places=2, max_digits = 5)
    selling_price    =  models.DecimalField(decimal_places=2, max_digits = 5)
    tax              =  models.DecimalField(decimal_places=2, max_digits = 5)
    date_added       =  models.DateField(max_length = 10)
    last_updated     =  models.DateTimeField(max_length = 10)
    is_active        =  models.BooleanField(max_length = 10)

    def __str__(self):
        return self.item_id
