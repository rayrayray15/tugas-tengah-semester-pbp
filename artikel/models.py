from django.db import models
from django.urls import reverse
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile

class Artikel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    image_file = models.ImageField(upload_to='images', blank=True)
    image_url = models.URLField(blank=True)
    slug = models.SlugField(null=False, unique=True, max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artikel_detail', args=[str(self.id)])

    def get_remote_image(self):
        if self.image_url and not self.image_file:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image_file.save(f"image_{self.pk}", File(img_temp))
        self.save()