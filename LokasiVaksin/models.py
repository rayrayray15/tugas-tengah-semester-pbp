from django.db import models

# Create your models here.
class Pulau(models.Model):
    NamaLokasi = models.CharField(max_length=20)
    
    def __str__(self):
        return self.NamaLokasi

class Vaksin(models.Model):
    NamaVaksin = models.CharField(max_length=20)
    def __str__(self):
        return self.NamaVaksin

class AddLokasi(models.Model):
    pulau = models.ForeignKey(Pulau, on_delete=models.CASCADE, null=True)
    NamaLokasi = models.CharField(max_length=20)
    JenisVaksin = models.ForeignKey(Vaksin, on_delete=models.CASCADE, null=True)
    RincianDosis = models.CharField(max_length=20)
    Alamat = models.TextField()
    

    def __str__(self):
        return self.NamaLokasi


