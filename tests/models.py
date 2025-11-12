from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

class TestCase(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name="Fan"
    )
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "TestCase"
        verbose_name_plural = "TestCaselar"

class Test(models.Model):

    test_score = models.FloatField(verbose_name="Savol bali", default=0)
    testcase = models.ForeignKey(
        TestCase,
        on_delete=models.CASCADE,
        verbose_name="Testcase",
        related_name="tests", 
    )

    question = models.TextField(verbose_name="Savol")

    answer_a = models.CharField(max_length=1024, verbose_name="A variant")
    answer_b = models.CharField(max_length=1024, verbose_name="B variant")
    answer_c = models.CharField(max_length=1024, verbose_name="C variant")
    answer_d = models.CharField(max_length=1024, verbose_name="D variant")

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A','A'),
            ('B','B'),
            ('C','C'),
            ('D','D'),
        ],
        verbose_name="Tog'ri javob"
    )

    def __str__(self):
        return f"{self.testcase}"

    class Meta:
        verbose_name="Test"
        verbose_name_plural="Testlar"