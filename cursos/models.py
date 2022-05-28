from django.db import models
from decimal import Decimal
from django.db.models import Avg
from django.db.models import signals


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    media = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.titulo

    def media_avaliacoes(self):
        aux_media = self.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if aux_media is None:
            self.media = Decimal(0)
        self.media = Decimal(round(aux_media * 2) / 2)


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'


def avaliacao_post_save(signal, instance, sender, **kwargs):
    instance.curso.media_avaliacoes()


signals.post_save.connect(avaliacao_post_save, sender=Avaliacao)
