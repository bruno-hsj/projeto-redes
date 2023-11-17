# -*- coding: utf-8 -*-
"""
@author: Marcos F. Caetano (mfcaetano@unb.br) 03/11/2020

@description: PyDash Project

Implementação do método proposto pelo artigo definido

"""

'''

Variaveis importantes para lembrar

quality_id - Taxa em que o video foi codificado (46980bps, ..., 4726737bps) 
qi         - indice de qualidade normalizado
segment_id - número de sequência do arquivo de video

Player is a Singleton class implementation

'''


from player.parser import *
from r2a.ir2a import IR2A

class R2ANewAlgoritm1(IR2A):

    def __init__(self, id):
        IR2A.__init__(self, id)
        self.parsed_mpd = ''
        self.qi = []

    def handle_xml_request(self, msg):
        self.send_down(msg)

    def handle_xml_response(self, msg):
        # Realiza um get da lista de qualidades disponíveis - getting qi list
        self.parsed_mpd = parse_mpd(msg.get_payload())
        self.qi = self.parsed_mpd.get_qi()

        self.send_up(msg)

    def handle_segment_size_request(self, msg):
        # Definicao da qualidade do segmento - Algoritmo ABR
        
        self.send_down(msg)

    def handle_segment_size_response(self, msg):

        self.send_up(msg)

    def initialize(self):
        pass

    def finalization(self):
        pass
