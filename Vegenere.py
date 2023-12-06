import math

class Vegenere:
    def __init__(self):
        self.keyword = 'crystalgems'

    ## Define uma nova palavra-chave
def set_keyword(self, keyword):
    self.keyword = keyword

## Retorna a mensagem criptografada
def get_encrypted_message(self, mensagem):

    palavra_chave = self.__fit_keyword(mensagem)
    mensagem_criptografada = ''     
    for i, letra in enumerate(mensagem):
        mensagem_criptografada += self.__get_encrypted_letter(palavra_chave[i], letra)
    
    return mensagem_criptografada

# Retorna a mensagem original (string) a partir da mensagem criptografada
def get_original_message(self, mensagem):

    palavra_chave = self.__fit_keyword(mensagem)  
    mensagem_original = ''
    for i, letra in enumerate(mensagem):
        mensagem_original += self.__get_original_letter(palavra_chave[i], letra)
    
    return mensagem_original

## Retorna uma lista da mensagem inteira em binário
@staticmethod
def string_to_binary(mensagem):
    mensagem_binaria_str = ''
    for letra in mensagem:
        mensagem_binaria_str += bin(ord(letra))[2:].zfill(8)

    mensagem_binaria = []
    for letra in mensagem_binaria_str:
        i = 0
        if letra == '1':
            i = 1
        mensagem_binaria.append(i)

    return mensagem_binaria

## Converte cada byte em caracteres
@staticmethod
def binary_to_string(binario):
    mensagem_binaria = [binario[i:i + 8] for i in range(0, len(binario), 8)]
    
    mensagem = ''
    for byte in mensagem_binaria:
        mensagem += chr(int(''.join([str(item) for item in byte]), 2))
    
    return mensagem

## Retorna a mensagem binária criptografada
def encode_vegenere(self, mensagem):
    mensagem_criptografada = self.get_encrypted_message(mensagem)
    mensagem_binaria = self.string_to_binary(mensagem_criptografada)
    return mensagem_binaria

## Retorna a mensagem binária criptografada para a mensagem original
def decodeVegenere(self, mensagem_binaria):
    mensagem_criptografada = self.binary_to_string(mensagem_binaria)
    mensagem_original = self.get_original_message(mensagem_criptografada)
    return mensagem_original
