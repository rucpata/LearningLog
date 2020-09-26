from django.db import models

# Create your models here.
class Topic(models.Model):
    """Temat poznawany przez uzytkownika."""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return self.text

class Entry(models.Model):
    """Konkretnre inforamcje o postępie w nauce"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Zwraca reprezentuację modelu w postaci ciągu tekstopwego."""
        if len(self.text) >= 50:
            return self.text[:50] + '...'
        else:
            return self.text