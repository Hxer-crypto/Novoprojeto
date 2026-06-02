from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views import (
    IndexView,
    JogadoresView,
    TreinosView,
    PresencasView,
    PartidasView,
    MensalidadesView,
    AvisosView,

    ComissaoTecnicaView,
    CampeonatosView,
    LocaisView,
    EstatisticasView,
    EscalacoesView,
    PatrocinadoresView,
    CalendarioView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('jogadores/', JogadoresView.as_view(), name='jogadores'),

    path('treinos/', TreinosView.as_view(), name='treinos'),

    path('presencas/', PresencasView.as_view(), name='presencas'),

    path('partidas/', PartidasView.as_view(), name='partidas'),

    path('mensalidades/', MensalidadesView.as_view(), name='mensalidades'),

    path('avisos/', AvisosView.as_view(), name='avisos'),

    path('comissao/', ComissaoTecnicaView.as_view(), name='comissao'),

    path('campeonatos/', CampeonatosView.as_view(), name='campeonatos'),

    path('locais/', LocaisView.as_view(), name='locais'),

    path('estatisticas/', EstatisticasView.as_view(), name='estatisticas'),

    path('escalacoes/', EscalacoesView.as_view(), name='escalacoes'),

    path('patrocinadores/', PatrocinadoresView.as_view(), name='patrocinadores'),

    path('calendario/', CalendarioView.as_view(), name='calendario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)