from django.db import models

class Score(models.Model):
    test = models.OneToOneField(
        'tests.TestCase',
        on_delete=models.CASCADE,
        verbose_name='Test',
    )
    score = models.FloatField(default=True)
    bilish = models.FloatField(default=0)
    bilish_count = models.IntegerField(default=0)
    qollash = models.FloatField(default=0)
    qollash_count = models.FloatField(default=0)
    muhokama = models.FloatField(default=0)
    muhokama_count = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.test}"
    
    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
