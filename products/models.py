from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    depth = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.parent:
            self.depth = self.parent.depth + 1
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    images = models.ManyToManyField('Image', related_name='products')
    videos = models.ManyToManyField('Video', related_name='products')
    views = models.PositiveIntegerField(default=0)


class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')


class Video(models.Model):
    video = models.FileField(upload_to='product_videos/')


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
