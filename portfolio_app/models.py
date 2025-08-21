from django.db import models

class DownloadCV(models.Model):
    cv = models.FileField(upload_to='updated_cv')

class Projects(models.Model):
    CATEGORY_CHOICES = [
    ('personal', 'personal'),
    ('production', 'production'),
    ('academic', 'academic'),
    ]

    title = models.CharField(max_length=50)
    category = models.CharField(max_length=75, choices=CATEGORY_CHOICES)
    github_link = models.TextField(null=True, blank=True)
    is_deployed = models.BooleanField(default=False)
    deployed_link = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField()

class Languages(models.Model):
    language = models.CharField(max_length=50) 
    rate = models.CharField(max_length=101, default='0')

class Skills(models.Model): 
    skill = models.CharField(max_length=88)

class Awards(models.Model): 
    name = models.CharField(max_length=200)

class Educations(models.Model):
    venue = models.CharField(max_length=100)
    degree = models.CharField(max_length=30)
    year = models.CharField(max_length=70)

class Experiences(models.Model):
    company = models.CharField(max_length=155)
    role = models.CharField(max_length=155)
    year = models.CharField(max_length=69)

class Icons(models.Model):
    link = models.CharField(max_length=255)
    class_link = models.CharField(max_length=111)