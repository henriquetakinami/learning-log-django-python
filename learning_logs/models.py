from django.db import models

# Create your models here.

class Topic(models.Model):
    """Um assunto novo para o usuário, de aprendizado"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma String de representação"""
        return self.text

class Entry(models.Model):
    """O que eu aprendi sobre determinado assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação da String como modelo"""
        return self.text[:50] + "..."

