from django.db import models
from django.utils import timezone
from datetime import date
from accounts.models import ProfileUser
#https://docs.djangoproject.com/en/2.2/ref/models/fields/


# class Kind(models.Model):
#     kind_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return f"{self.kind_name}"

#https://docs.djangoproject.com/en/2.2/topics/i18n/timezones/
class Tree(models.Model):

    KIND_CHOICES = (
        ('', 'Select Kind'),
        ('A', 'Ash tree'),
        ('B', 'Bush'),
        ('C', 'Chestnut Oak'),
        ('E', 'English Oak tree'),
        ('F', 'Flower'),
        ('G', 'Grass'),
        ('I', 'Birch tree'),
        ('L', 'Linden tree'),
        ('M', 'Elm tree'),
        ('О', 'Poplar tree'),
        ('P', 'Plane tree'),
        ('R', 'Мulberry tree'),
        ('S', 'Spruse tree'),
        ('U', 'Paulovnia tree'),
        ('Y', 'Cypress tree'),
        ('W', 'White Oak'),


    )
    DISTRICT_CHOICES = (
        ('', 'Select District'),
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
        ('', 'Select Type'),
        ('B', 'Bush'),
        ('F', 'Flower'),
        ('G', 'Grass'),
        ('T', 'Tree'),
    )

    LIFECYCLE = (
        ('', 'Select Lifecycle Status'),
        ('A', 'Healthy'),
        ('I', 'Unhealthy'),
        ('P', 'Passed'),

    )

    type = models.CharField(blank=False,max_length=1, choices=TYPE_CHOICES)
    kind = models.CharField(blank=False,max_length=1, choices=KIND_CHOICES)
    # kind = models.ForeignKey(Kind, on_delete=models.CASCADE, blank=True)
    latin_name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    origin_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    lifecycle_status = models.CharField(blank=False,max_length=1, choices=LIFECYCLE)
    size = models.PositiveIntegerField(blank=True,null=True)
    district = models.CharField(blank=False,max_length=1, choices=DISTRICT_CHOICES)
    latitude = models.DecimalField(max_digits=8,decimal_places=6,error_messages= {'required': "Please, fill with the format specified",'invalid': "Please, use the format specified"})
    longitude = models.DecimalField(max_digits=9,decimal_places=6,error_messages= {'required': "Please, fill with the format specified",'invalid': "Please, use the format specified"})
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.pk}, {self.get_kind_display()}, {self.get_district_display()}'
        #return self.get_kind_display()

#https://support.google.com/maps/answer/18539?co=GENIE.Platform%3DDesktop&hl=en
#http://soilquality.org/indicators.html


class Task(models.Model):
    TASK_TYPE_CHOICES = (
        ('', 'Select Task Type'),
        ('C', 'Cut'),
        ('F', 'Fertilize'),
        ('L', 'Picking Leaves'),
        ('P', 'Plant'),
        ('T', 'Trim'),
        ('W', 'Water'),

    )
    STATUS_CHOICES = (
        ('', 'Select Task Status'),
        ('A', 'Active'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
        ('S', 'Skipped'),
    )
    GENERATION_CHOICES = (
        ('', 'Select Generation Type'),
        ('A', 'Automatic'),
        ('M', 'Manual'),
    )
    task_type = models.CharField(blank=False,max_length=1, choices=TASK_TYPE_CHOICES)
    status = models.CharField(blank=False,max_length=1, choices=STATUS_CHOICES)
    date_generated = models.DateField(default=date.today)
    date_completed = models.DateField(blank=True,null=True)
    generation = models.CharField(blank=False,max_length=1, choices=GENERATION_CHOICES)
    description = models.TextField(blank=True,null=True)
    task_force = models.CharField(blank=True,null=True,max_length=200)
    cost = models.DecimalField(blank=True,null=True,max_digits=8, decimal_places=2)
    trees = models.ManyToManyField(Tree)
    user = models.ForeignKey(ProfileUser,on_delete=models.CASCADE)

    @property
    def all_trees(self):
        return '; '.join([str(x) for x in self.trees.all()]) # here it was x.get_kind_display() instead of str(x)