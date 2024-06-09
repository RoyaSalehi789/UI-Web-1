from django.db import models


class siteBanner(models.Model):
    class siteBannerPositions(models.TextChoices):
        home_page = 'home_page', 'صفحه اصلی'
        product_list = 'product_list', 'صفحه لیست محصولات',
        product_detail = 'product_detail', 'صفحه جزئیات محصولات',
        about_us = 'about_us', 'درباره ما'

    title = models.CharField(max_length=200, verbose_name='banner title')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='banner address')
    image = models.ImageField(upload_to='uploads/images/banners', verbose_name='banner image')
    is_active = models.BooleanField(verbose_name='active/inactive')
    position = models.CharField(max_length=200, choices=siteBannerPositions.choices, verbose_name='banner position')

    def __str__(self):
        return self.title

    class Metta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
