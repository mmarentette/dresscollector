from django.db import models
from django.urls import reverse

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
    
    # Django recommends get_absolute_url method in Model instead of success_url in view function because it will redirect the user after they either create OR update a dress (instead of defining a success_url in both view functions)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dress_id': self.id})
        # reverse function is similar to url tag; redirects user to appropriate path (detail) and populates necessary route parameters from kwargs (dress_id)
