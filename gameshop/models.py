from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=256, unique=True, db_index=True, verbose_name='Kategoria', blank=False) #nazwa kategorii, do ktorej bedzie nalezala gra
    slug = models.SlugField(max_length=256, unique=True, blank=False) #a to nazwa, ktora bedzie wyswietlana w url strony, czyli bez znakow specjalnych itp

    class Meta:
        verbose_name_plural = 'Kategorie' #nazwa wyswietlana u admina
    
    def __str__(self):
        return self.category
    
class Developer(models.Model):
    developer = models.CharField(max_length=256, unique=True, db_index=True, verbose_name='Nazwa developera', blank=False)
    slug = models.SlugField(max_length=256, unique=True, blank=False)

    class Meta:
        verbose_name_plural = 'Developerzy'

    def __str__(self):
        return self.developer

class Game(models.Model):
    category = models.ForeignKey(Category, related_name='cat', on_delete=models.CASCADE, verbose_name='Kategoria')
    developer = models.ForeignKey(Developer, related_name='dev', on_delete=models.CASCADE, verbose_name='Developer')
    title = models.CharField(max_length=256, verbose_name='Tytuł', blank=False)
    description = models.TextField(blank=True, verbose_name='Opis')
    instock = models.BooleanField(default=False, verbose_name='Dostępność', blank=False)
    price = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='Cena', blank=False)
    release_date = models.DateField(verbose_name='Data wydania', blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')
    image = models.ImageField()
    slug = models.SlugField(max_length=256, unique=True, blank=False)

    class Meta:
        verbose_name_plural = 'Gry' #nazwa wyswietlana u admina
    
    def url_get(self):
        return reverse('gameshop:game', args=[self.slug])

    def __str__(self):
        return self.title
    





