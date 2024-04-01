from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    laundry_id = models.CharField(max_length=10, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    kilo = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Pending")
    is_ready = models.BooleanField(default=False)
    is_claimed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Generate laundry_id if it's not set
        if not self.laundry_id:
            latest_order = Order.objects.order_by('-id').first()
            if latest_order:
                last_id = int(latest_order.laundry_id[2:])  # Extract the numeric part
                new_id = 'LD{:03d}'.format(last_id + 1)  # Increment the numeric part and format
            else:
                new_id = 'LD001'  # If no orders exist yet
            self.laundry_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.laundry_id
