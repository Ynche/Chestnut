from django.db import models
from django.utils import timezone
from datetime import date
#https://docs.djangoproject.com/en/2.2/ref/models/fields/



#https://docs.djangoproject.com/en/2.2/topics/i18n/timezones/
class Tree(models.Model):

    KIND_CHOICES = (
        ('0', ' '),
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
        ('0', '  '),
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
        ('0', ' '),
        ('B', 'Bush'),
        ('F', 'Flower'),
        ('G', 'Grass'),
        ('T', 'Tree'),
    )

    TYPE = (
        ('B', 'Bush'),
        ('F', 'Flower'),
        ('G', 'Grass'),
        ('T', 'Tree'),
    )
    LIFECYCLE = (
        ('0', ' '),
        ('A', 'Healthy'),
        ('I', 'Unhealthy'),
        ('P', 'Passed'),

    )

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    latin_name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    origin_date = models.DateField(help_text="Use the following format:YYYY-MM-DD")
    end_date = models.DateField(help_text="Use the following format:YYYY-MM-DD",blank=True,null=True)
    lifecycle_status = models.CharField(max_length=1, choices=LIFECYCLE)
    size = models.PositiveIntegerField(blank=True)
    district = models.CharField(max_length=1, choices=DISTRICT_CHOICES)
    latitude = models.DecimalField(max_digits=7,decimal_places=5)
    longitude = models.DecimalField(max_digits=8,decimal_places=5)



    def __str__(self):
        return f'{self.pk}, {self.get_kind_display()}, {self.get_district_display()}'
        #return self.get_kind_display()

#https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=en
#http://soilquality.org/indicators.html


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
    date_generated = models.DateField(default=date.today)
    date_completed = models.DateField(blank=True,null=True)
    generation = models.CharField(max_length=1, choices=GENERATION_CHOICES)
    description = models.TextField(blank=True,null=True)
    task_force = models.CharField(max_length=200)
    cost = models.DecimalField(blank=True,null=True,max_digits=8, decimal_places=2)
    trees = models.ManyToManyField(Tree)