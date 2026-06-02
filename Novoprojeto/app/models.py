from django.db import models


class Jogador(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do jogador")
    posicao = models.CharField(max_length=50, verbose_name="Posição")
    numero_camisa = models.IntegerField(
        verbose_name="Número da camisa",
        null=True,
        blank=True
    )
    telefone = models.CharField(
        max_length=20,
        verbose_name="Telefone",
        blank=True
    )
    email = models.CharField(
        max_length=100,
        verbose_name="Email",
        blank=True
    )
    ativo = models.BooleanField(
        default=True,
        verbose_name="Ativo no time"
    )

    def __str__(self):
        return f"{self.nome} - #{self.numero_camisa}"

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"


class Treino(models.Model):
    data = models.DateField(verbose_name="Data do treino")
    horario = models.TimeField(verbose_name="Horário")
    local = models.CharField(max_length=200, verbose_name="Local")
    descricao = models.CharField(
        max_length=300,
        verbose_name="Descrição",
        blank=True
    )

    def __str__(self):
        return f"Treino - {self.data} às {self.horario}"

    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"


class PresencaTreino(models.Model):
    STATUS_CHOICES = [
        ('presente', 'Presente'),
        ('ausente', 'Ausente'),
        ('justificado', 'Justificado'),
    ]

    jogador = models.ForeignKey(
        Jogador,
        on_delete=models.CASCADE,
        verbose_name="Jogador"
    )

    treino = models.ForeignKey(
        Treino,
        on_delete=models.CASCADE,
        verbose_name="Treino"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Status"
    )

    def __str__(self):
        return f"{self.jogador.nome} - {self.treino.data} - {self.status}"

    class Meta:
        verbose_name = "Presença em Treino"
        verbose_name_plural = "Presenças em Treinos"


class Partida(models.Model):
    TIPO_CHOICES = [
        ('amistoso', 'Amistoso'),
        ('campeonato', 'Campeonato'),
    ]

    adversario = models.CharField(
        max_length=100,
        verbose_name="Adversário"
    )

    data = models.DateField(verbose_name="Data da partida")

    horario = models.TimeField(verbose_name="Horário")

    local = models.CharField(
        max_length=200,
        verbose_name="Local"
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        verbose_name="Tipo"
    )

    gols_pro = models.IntegerField(
        verbose_name="Gols a favor",
        null=True,
        blank=True
    )

    gols_contra = models.IntegerField(
        verbose_name="Gols contra",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"vs {self.adversario} - {self.data}"

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"


class Mensalidade(models.Model):
    STATUS_CHOICES = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
        ('atrasado', 'Atrasado'),
    ]

    jogador = models.ForeignKey(
        Jogador,
        on_delete=models.CASCADE,
        verbose_name="Jogador"
    )

    mes_referencia = models.CharField(
        max_length=20,
        verbose_name="Mês de referência"
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Valor (R$)"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Status"
    )

    data_pagamento = models.DateField(
        verbose_name="Data do pagamento",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.jogador.nome} - {self.mes_referencia} - {self.status}"

    class Meta:
        verbose_name = "Mensalidade"
        verbose_name_plural = "Mensalidades"


class Aviso(models.Model):
    titulo = models.CharField(
        max_length=150,
        verbose_name="Título"
    )

    mensagem = models.TextField(
        verbose_name="Mensagem"
    )

    data_publicacao = models.DateField(
        auto_now_add=True,
        verbose_name="Data de publicação"
    )

    importante = models.BooleanField(
        default=False,
        verbose_name="Importante"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Aviso"
        verbose_name_plural = "Avisos"


class ComissaoTecnica(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Comissão Técnica"
        verbose_name_plural = "Comissões Técnicas"

    def __str__(self):
        return f"{self.nome} - {self.cargo}"


class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    organizador = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    class Meta:
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"

    def __str__(self):
        return self.nome


class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"

    def __str__(self):
        return self.nome


class EstatisticaJogador(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    gols = models.IntegerField(default=0)
    assistencias = models.IntegerField(default=0)
    cartoes_amarelos = models.IntegerField(default=0)
    cartoes_vermelhos = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Estatística de Jogador"
        verbose_name_plural = "Estatísticas de Jogadores"

    def __str__(self):
        return self.jogador.nome


class Escalacao(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    titular = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Escalação"
        verbose_name_plural = "Escalações"

    def __str__(self):
        return f"{self.partida} - {self.jogador}"


class Patrocinador(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    imagem = models.ImageField(upload_to='patrocinadores/', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"


class EventoCalendario(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = "Evento do Calendário"
        verbose_name_plural = "Eventos do Calendário"

    def __str__(self):
        return self.titulo