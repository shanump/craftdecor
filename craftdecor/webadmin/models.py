from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image
from django.core.files.base import ContentFile



class Categories(models.Model):
    cat_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_avail = models.BooleanField(default=False)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cat_name

    def save(self, *args, **kwargs):
        self.thumbnail = self.crop_image(self.image)
        super().save(*args, **kwargs)  

    def crop_image(self, image):

        img = Image.open(image)

        # Define the desired size
        desired_size = (370, 250)

         # Calculate the cropping box
        img_ratio = image.width / image.height
        target_ratio = desired_size[0] / desired_size[1]

        if img_ratio > target_ratio:
            # Wider than target
            new_height = img.height
            new_width = int(new_height * target_ratio)
            offset = (img.width - new_width) // 2
            crop_box = (offset, 0, offset + new_width, new_height)
        else:
            # Taller than target
            new_width = img.width
            new_height = int(new_width / target_ratio)
            offset = (img.height - new_height) // 2
            crop_box = (0, offset, new_width, offset + new_height)
        
        img = img.crop(crop_box)

        # Resize the image
        img = img.resize(desired_size, Image.Resampling.LANCZOS)

        img.convert('RGB')
        #img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        croped_image = File(thumb_io, name=image.name)

        return croped_image


class Products(models.Model):
    pro_name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, related_name='items', on_delete=models.DO_NOTHING)
    tag = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_avail = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.pro_name

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)
        super().save(*args, **kwargs)  

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail