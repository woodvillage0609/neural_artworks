from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils import timezone
from neuralStyleProcess import neuralStyleTransfer

# Create your models here.

ACTION_CHOICES = (
    ('UDNIE', 'Udnie'),
    ('CANDY', 'Candy'),
    ('MOSAIC', 'Mosaic'),
    ('PINK', 'Pink'),
    ('SCREAM', 'Scream'),
    ('LA_MUSE', 'La Muse'),
    # ('FIRE', 'Fire'),
    # ('FLAME', 'Flame'),
    ('RAIN', 'Rain'),
    ('LANDSCAPE', 'Landscape'),
    # ('GOLD_BLACK', 'Gold Black'),
    ('TRIANGLE', 'Triangle'),
    # ('STARRY_NIGHT', 'Starry Night'),
    # ('STARRY_NIGHT_2500', 'Starry Night2'),
    # ('WAVE', 'Wave'),
    # ('FEATHERS', 'Feathers'),
    # ('COMPOSITION', 'Composition')

)

class Arts(models.Model):
    image = models.ImageField(upload_to='pictures/')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #以下を追加。新規POST後に、どのURLに飛ばすか指定するためのもの
    def get_absolute_url(self):
        return reverse( 'art-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):

        # open image
        pil_img = Image.open(self.image)

        # convert an image to array and do some processing
        cv_img = np.array(pil_img)

        img = neuralStyleTransfer(cv_img, self.action)

        # convert back to pil image
        im_pil = Image.fromarray(img)
        # im_pil = Image.fromarray((img * 255).astype(np.uint8))

        #圧縮クオリティ
        COMPRESS_QUALITY = 20

        # save
        buffer = BytesIO()
        
        im_pil.save(buffer, format='png', quality = COMPRESS_QUALITY)
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)


class Like(models.Model):
    art = models.ForeignKey(Arts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
