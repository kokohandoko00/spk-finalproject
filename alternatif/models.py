# Model merupakan pendefinisian seluruh variabel input
from django.db import models
class alternatif(models.Model):
    kodealternatif = models.CharField(max_length=3, primary_key=True)
    namaalternatif = models.CharField(max_length=25)
    c1 = models.FloatField()
    suhu= (
        (1, '< 0℃'),
        (2, '0℃ - 15℃'),
        (3, '> 15℃'),
    )
    # c2 = models.FloatField(choices=suhu, default=1)
    c2 = models.FloatField(choices=suhu)
    angka= (
        (1, 'KURANG MENDUKUNG'),
        (2, 'CUKUP MENDUKUNG'),
        (3, 'SANGAT MENDUKUNG'),
    )
    c3 = models.FloatField(choices=angka)
    krim = (
        (1, '< 40'),
        (2, '40 - 60'),
        (3, '> 60'),
    )
    c4 = models.FloatField(choices=krim)
    oleh = (
        (1, '< Rp 3.000.000'),
        (2, 'Rp 3.000.000 - Rp 5.000.000'),
        (3, '> Rp 5.000.000'),
    )
    c5 = models.FloatField(choices=oleh)

    def __str__(self):
        return "{}". format(self.kodealternatif)
class normalisasi(models.Model):
    kodealternatif = models.CharField(max_length=3)
    c1norm = models.IntegerField()
    c2norm = models.IntegerField()
    c3norm = models.IntegerField()
    c4norm = models.IntegerField()
    c5norm = models.IntegerField()
    def __str__(self):
        return "{}". format(self.kodealternatif)