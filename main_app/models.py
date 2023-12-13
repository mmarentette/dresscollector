from django.db import models
from django.urls import reverse
from django.utils import timezone

RATING_CHOICES = [(i, i) for i in range(1, 6)]

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

class Review(models.Model):
    created_at = models.DateTimeField(default=timezone.now) # Swapping what's in parens for auto_now_add=True would work too (limitation: we wouldn't be able to modify this field, which should also be fine in this cased)
    reviewer_name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(
        choices=RATING_CHOICES,
        default=RATING_CHOICES[-1][-1],
    )
    text = models.TextField('Comments and Feedback', max_length=300)

    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)
    # Note that the column for FK in the reviews table will be called dress_id (Django default behaviour)
    # First argument: parent Model
    # on_delete=models.CASCADE is required or one-to-many relationships. If a Dress record is delete, all child Reviews will be deleted automatically as well - prevents 'orphan' records

    def __str__(self):
        return f"{self.reviewer_name} ({self.rating}): {self.text}"
