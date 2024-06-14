from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    class productCategory(models.TextChoices):
        Mobile_Phones = 'Mobile_Phones', 'Mobile Phones'
        Smart_TV = 'Smart_TV', 'Smart TV',
        Smart_Watch = 'Smart_Watch', 'Smart Watch',
        Laptops = 'Laptops', 'Laptops',
        Drones = 'Drones', 'Drones',
        Headphones = 'Headphones', 'Headphones'

    name = models.CharField(max_length=255, choices=productCategory.choices)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    depth = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.parent:
            self.depth = self.parent.depth + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=355, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(default="", null=False, db_index=True)
    brand = models.CharField(max_length=200, default="")
    item_height = models.DecimalField(max_digits=50, default=0, decimal_places=2)
    item_width = models.DecimalField(max_digits=50, default=0, decimal_places=2)
    screen_size = models.DecimalField(max_digits=50, default=0, decimal_places=2)
    model_number = models.CharField(max_length=200, default="")
    ram_size = models.DecimalField(max_digits=200, default=0, decimal_places=2)
    operating_system = models.CharField(max_length=100, default="")
    set_as_banner = models.BooleanField(default=False)
    set_as_site_background = models.BooleanField(default=False)
    slogan = models.TextField(default="")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])


class Image(models.Model):
    product = models.ManyToManyField('Product', related_name='images')
    image = models.ImageField(upload_to='images/product_images/')
    title = models.CharField(max_length=100, default="", choices=[('off-box', 'Off-box'),
                                                                  ('detail-box', 'Detail-box'),
                                                                  ('banner', 'Banner'),
                                                                  ('background', 'Background')])

    def __str__(self):
        products = ', '.join([product.name for product in self.product.all()])
        return f"{self.title} - Products: {products}"

    class Metta:
        verbose_name = 'image gallery'
        verbose_name_plural = 'images gallery'


class Video(models.Model):
    video = models.FileField(upload_to='product_videos/')
    product = models.ManyToManyField('Product', related_name='video')


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
