from django.db import models
from django.utils import timezone

class Score(models.Model):
    test = models.ForeignKey(
        'tests.TestCase',
        on_delete=models.CASCADE,
        verbose_name='Test',
    )

    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name='User'
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

    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.test}"
    
    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
