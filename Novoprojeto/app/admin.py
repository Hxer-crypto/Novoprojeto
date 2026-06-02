from django.contrib import admin
from .models import *

admin.site.register(Jogador)
admin.site.register(Treino)
admin.site.register(PresencaTreino)
admin.site.register(Partida)
admin.site.register(Mensalidade)
admin.site.register(Aviso)

admin.site.register(ComissaoTecnica)
admin.site.register(Campeonato)
admin.site.register(Local)
admin.site.register(EstatisticaJogador)
admin.site.register(Escalacao)
admin.site.register(Patrocinador)
admin.site.register(EventoCalendario)