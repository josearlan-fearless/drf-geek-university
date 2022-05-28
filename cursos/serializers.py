from rest_framework import serializers
from .models import Curso, Avaliacao

import numpy as np
from decimal import Decimal
from django.db.models import Avg


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    def validate_avaliacao(self, valor):
        lista = []
        for i in np.arange(1, 5.1, 0.1):
            aux = Decimal(format(i, ".1f"))
            lista.append(aux)

        if valor in lista:
            return valor
        raise serializers.ValidationError('A Avaliação precisa ser um inteiro entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    """
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail')
    """
    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media'
        )
