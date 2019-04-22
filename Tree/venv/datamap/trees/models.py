from django.db import models


class Tree(models.Model):
    TYPE_CHOICES = (
        ('A', 'Ash tree'),
        ('L', 'Linden tree'),
        ('P', 'Poplar tree'),
        ('B', 'Birch tree'),
        ('P', 'Plane tree'),
        ('U', 'Paulovnia tree'),
        ('M', 'Elm tree'),
        ('C', 'Chestnut Oak'),
        ('W', 'White Oak'),
        ('E', 'English Oak tree'),

    )
    DISTRICT_CHOICES = (
        ('B', 'Bankya'),
        ('H', 'Vitosha'),
        ('R', 'Vrabnitsa'),
        ('V', 'Vazrazhdane'),
        ('Z', 'Izgrev'),
        ('I', 'Ilinden'),
        ('Q', 'Iskar'),
        ('Y', 'Krasna polyana'),
        ('A', 'Krasno selo'),
        ('K', 'Kremikovtsi'),
        ('W', 'Lozenets'),
        ('L', 'Lyulin'),
        ('M', 'Mladost'),
        ('J', 'Nadezhda'),
        ('N', 'Novi Iskar'),
        ('U', 'Ovcha kupel'),
        ('O', 'Oborishte'),
        ('P', 'Pancharevo'),
        ('D', 'Poduene'),
        ('S', 'Serdika'),
        ('G', 'Slatina'),
        ('C', 'Studentski'),
        ('E', 'Sredets'),
        ('T', 'Triaditsa'),

    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    latin_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    age = models.PositiveIntegerField(blank=True)
    size = models.PositiveIntegerField(blank=True)
    district = models.CharField(max_length=1, choices=DISTRICT_CHOICES)
    latitude = models.DecimalField(max_digits=7,decimal_places=5)
    longitude = models.DecimalField(max_digits=8,decimal_places=5)
    



    def __str__(self):
        return f"{self.name}, kind {self.kind}"

#https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=en