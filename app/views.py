from django.shortcuts import render
from django.views import View

from .models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        avisos = Aviso.objects.order_by('-data_publicacao')[:5]
        total_jogadores = Jogador.objects.filter(ativo=True).count()
        proxima_partida = Partida.objects.order_by('data').first()

        return render(request, 'index.html', {
            'avisos': avisos,
            'total_jogadores': total_jogadores,
            'proxima_partida': proxima_partida,
        })


class JogadoresView(View):
    def get(self, request, *args, **kwargs):
        jogadores = Jogador.objects.all()

        return render(request, 'jogadores.html', {
            'jogadores': jogadores
        })


class TreinosView(View):
    def get(self, request, *args, **kwargs):
        treinos = Treino.objects.order_by('-data')

        return render(request, 'treinos.html', {
            'treinos': treinos
        })


class PresencasView(View):
    def get(self, request, *args, **kwargs):
        presencas = PresencaTreino.objects.all()

        return render(request, 'presencas.html', {
            'presencas': presencas
        })


class PartidasView(View):
    def get(self, request, *args, **kwargs):
        partidas = Partida.objects.order_by('-data')

        return render(request, 'partidas.html', {
            'partidas': partidas
        })


class MensalidadesView(View):
    def get(self, request, *args, **kwargs):
        mensalidades = Mensalidade.objects.all()

        return render(request, 'mensalidades.html', {
            'mensalidades': mensalidades
        })


class AvisosView(View):
    def get(self, request, *args, **kwargs):
        avisos = Aviso.objects.order_by('-data_publicacao')

        return render(request, 'avisos.html', {
            'avisos': avisos
        })


class ComissaoTecnicaView(View):
    def get(self, request, *args, **kwargs):
        membros = ComissaoTecnica.objects.all()

        return render(request, 'comissao_tecnica.html', {
            'membros': membros
        })


class CampeonatosView(View):
    def get(self, request, *args, **kwargs):
        campeonatos = Campeonato.objects.all()

        return render(request, 'campeonatos.html', {
            'campeonatos': campeonatos
        })


class LocaisView(View):
    def get(self, request, *args, **kwargs):
        locais = Local.objects.all()

        return render(request, 'locais.html', {
            'locais': locais
        })


class EstatisticasView(View):
    def get(self, request, *args, **kwargs):
        estatisticas = EstatisticaJogador.objects.all()

        return render(request, 'estatisticas.html', {
            'estatisticas': estatisticas
        })


class EscalacoesView(View):
    def get(self, request, *args, **kwargs):
        escalacoes = Escalacao.objects.all()

        return render(request, 'escalacoes.html', {
            'escalacoes': escalacoes
        })


class PatrocinadoresView(View):
    def get(self, request, *args, **kwargs):
        patrocinadores = Patrocinador.objects.all()

        return render(request, 'patrocinadores.html', {
            'patrocinadores': patrocinadores
        })


class CalendarioView(View):
    def get(self, request, *args, **kwargs):
        eventos = EventoCalendario.objects.all()

        return render(request, 'calendario.html', {
            'eventos': eventos
        })