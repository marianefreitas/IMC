from django.test import TestCase
from app.models import Turma


class TestModels(TestCase):

    def setUp(self):
        self.turma = Turma.objects.create(
            codigoTurma='5263',
            dataInicio='2002-10-10',
            descricao='6B'
        )

        self.assertEqual(self.turma.descricao, '6B')
