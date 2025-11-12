from django.db import models

class Score(models.Model):
    test = models.ForeignKey(
        'tests.TestCase',
        on_delete=models.CASCADE,
        verbose_name='Test',
    )
    score = models.FloatField(default=True)


    def __str__(self):
        return f"{self.test}"
    
    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
