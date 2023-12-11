from django.db import models

# Create your models here.
class Dress(models.Model):
    STYLE_CHOICES = {
        'a_line': 'A-line',
        'ball_gown': 'Ball gown',
        'fit_and_flare': 'Fit-and-flare',
        'mermaid_trumpet': 'Mermaid or trumpet',
        'sheath': 'Sheath',
        'short': 'Short',
    }
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    collection = models.CharField(max_length=100)
    style = models.CharField(
        max_length=15,
        choices=STYLE_CHOICES,
    )

    def __str__(self):
        return f"{self.designer}: {self.name}"
