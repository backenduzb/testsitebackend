from accounts.models import User

class Score(models.Model):
    user = models.ForeignKey(User, related_name="scores", on_delete=models.CASCADE)
    test = models.ForeignKey('tests.TestCase', on_delete=models.CASCADE, verbose_name='Test')
    score = models.FloatField(default=0)
    bilish = models.FloatField(default=0)
    bilish_count = models.IntegerField(default=0)
    qollash = models.FloatField(default=0)
    qollash_count = models.IntegerField(default=0)
    muhokama = models.FloatField(default=0)
    muhokama_count = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.test}"

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"
        unique_together = ('user', 'test') 
