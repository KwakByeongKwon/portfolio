# models.py
from django.db import models

class CsvFile(models.Model):
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')

class SeoulCafeList(models.Model):
    name = models.CharField(max_length=255)
    gu = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cafe_class = models.CharField(max_length=255)
    cafe_menu = models.TextField()
    review_count = models.CharField(max_length=255)
    review_top3 = models.TextField()
    background_image_url = models.URLField()

    def __str__(self):
        return self.name
