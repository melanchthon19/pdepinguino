from django.db import models
from django.urls import reverse

NGRAM_CHOICES = [
        (1, 'monograma'),
        (2, 'bigrama',),
        (3, 'trigrama'),
        (4, 'tetragrama'),
]

TEN_CHOICES = [(i,i) for i in range(1, 11)]
THIRTY_CHOICES = [(i,i) for i in range(1, 11)]

class NerudagramModel(models.Model):
    name = 'Nerudagram Model Parameters'
    ngram = models.IntegerField(choices=NGRAM_CHOICES, verbose_name="Modelo de N-Grama")
    wpt = models.IntegerField(choices=TEN_CHOICES, verbose_name="Cantidad de palabras en el título")
    mwpl = models.IntegerField(choices=TEN_CHOICES, verbose_name="Cantidad máxima de palabras por verso")
    lpp = models.IntegerField(choices=THIRTY_CHOICES, verbose_name="Cantidad de versos del poema")

    title = models.CharField(max_length=126, blank=True)
    poem = models.CharField(max_length=64000, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.name

    def get_absolute_url(self):
        return reverse("nerudagramApp:detail", kwargs={'pk': self.pk})

class NerudagramHistory(models.Model):
    name = 'Nerudagram History'
    title = models.CharField(max_length=126, blank=True)
    poem = models.CharField(max_length=64000, blank=True)
    original = models.ForeignKey(NerudagramModel, related_name='poems', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + self.name
