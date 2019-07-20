from django.db import models

# Create your models here.

LANGUAGE_CHOICES = [
    ('ENG', 'English'),
    ('SPA', 'Spanish'),
    ('CHI', 'Chinese'),
    ('FRA', 'French'),
    ('GER', 'German'),
    ('HIN', 'Hindi'),
    ('JPN', 'Japanese'),
    ('AR', 'Arabic'),
]

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('JPY', 'Japanese Yen'),
    ('CNY', 'Chinese Yuan'),
    ('INR', 'Indian Rupee'),
    ('EUR', 'Euro'),
    ('GBP', 'Pound'),
]

class Provider(models.Model):
    """
    """
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    language = models.CharField(max_length = 3, choices = LANGUAGE_CHOICES)
    currency = models.CharField(max_length = 3, choices = CURRENCY_CHOICES)

    def __str__(self):
        return self.name
