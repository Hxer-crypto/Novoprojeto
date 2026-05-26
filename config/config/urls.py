from django.contrib import admin
from django.urls import path

from app.views import (
    IndexView,
    JogadoresView,
    TreinosView,
    PresencasView,
    PartidasView,
    MensalidadesView,
    AvisosView,
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
]