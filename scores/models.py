from django.db import models
from django.conf import settings

class Score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Foydalanuvchi',
        related_name='user_test_scores'  
    )
    test = models.ForeignKey(
        'tests.TestCase',
        on_delete=models.CASCADE,
        verbose_name='Test',
    )
    score = models.FloatField(default=0)
    bilish = models.FloatField(default=0)
    bilish_count = models.IntegerField(default=0)
    qollash = models.FloatField(default=0)
    qollash_count = models.FloatField(default=0)
    muhokama = models.FloatField(default=0)
    muhokama_count = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.test}"
    
    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
        unique_together = ['user', 'test']