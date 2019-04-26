from django.db import models
from django.utils import timezone


class Tree(models.Model):
    KIND = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    )
    TYPE = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('aaaaa', '.....'),
    )
    KIND_CHOICES = (
        ('0', '-------------------------------------------'),
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
        ('0', '--------------------------------------'),
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
    TYPE_CHOICES = (
        ('0', '----------------------------------------'),
        ('B', 'Bush'),
        ('F', 'Flower'),
        ('G', 'Grass'),
        ('T', 'Tree'),

    )

    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    latin_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    age = models.PositiveIntegerField(blank=True)
    size = models.PositiveIntegerField(blank=True)
    district = models.CharField(max_length=1, choices=DISTRICT_CHOICES)
    latitude = models.DecimalField(max_digits=7,decimal_places=5)
    longitude = models.DecimalField(max_digits=8,decimal_places=5)


    def __str__(self):
        return f"{self.district}, kind {self.kind}"

#https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=en


class Task(models.Model):
    TASK_TYPE_CHOICES = (
        ('C', 'Cut'),
        ('F', 'Fertilize'),
        ('L', 'Picking Leaves'),
        ('P', 'Plant'),
        ('T', 'Trim'),
        ('W', 'Water'),

    )
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
        ('S', 'Skipped'),
    )
    GENERATION_CHOICES = (
        ('A', 'Automatic'),
        ('M', 'Manual'),
    )
    task_type = models.CharField(max_length=1, choices=TASK_TYPE_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date_generated = models.DateField(default=timezone.now())
    date_completed = models.DateField()
    generation = models.CharField(max_length=1, choices=GENERATION_CHOICES)
    description = models.TextField(blank=True)
    task_force = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

#https://docs.djangoproject.com/en/2.2/topics/i18n/timezones/