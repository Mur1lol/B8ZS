class Transposicao:
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
      # Calcula o número de colunas necessárias
      num_colunas = len(texto) # chave
      if len(texto) % self.chave != 0:
          num_colunas += 1

      # Preenche a matriz com espaços em branco
      matriz = [[' ' for _ in range(num_colunas)] for _ in range(self.chave)]

      # Preenche a matriz com os caracteres do texto
      index = 0
      for col in range(num_colunas):
          for row in range(self.chave):
              if index < len(texto):
                  matriz[row][col] = texto[index]
                  index += 1

      # Lê a matriz para obter o texto cifrado
      texto_cifrado = ''
      for row in range(self.chave):
          for col in range(num_colunas):
              texto_cifrado += matriz[row][col]

      return texto_cifrado

    def decifrar(self, texto_cifrado):
      # Calcula o número de colunas necessárias
      num_colunas = len(texto_cifrado) # chave
      if len(texto_cifrado) % self.chave != 0:
          num_colunas += 1

      # Preenche a matriz com espaços em branco
      matriz = [[' ' for _ in range(num_colunas)] for _ in range(self.chave)]

      # Preenche a matriz com os caracteres do texto cifrado
      index = 0
      for row in range(self.chave):
          for col in range(num_colunas):
              if index < len(texto_cifrado):
                  matriz[row][col] = texto_cifrado[index]
                  index += 1

      # Lê a matriz para obter o texto original
      texto_original = ''
      for col in range(num_colunas):
          for row in range(self.chave):
              texto_original += matriz[row][col]

      return texto_original

    @staticmethod
    def texto_para_binario(texto):
        return ''.join(format(ord(char), '016b') for char in texto)

    @staticmethod
    def binario_para_texto(binario):
        return ''.join(chr(int(binario[i:i+16], 2)) for i in range(0, len(binario), 16))

    ## Retorna a mensagem binária criptografada
    def encode_transposicao(self, mensagem):
        mensagem_criptografada = self.cifrar(mensagem)
        mensagem_binaria = self.texto_para_binario(mensagem_criptografada)
        return mensagem_binaria

    ## Retorna a mensagem binária criptografada para a mensagem original
    def decode_transposicao(self, mensagem_binaria):
        mensagem_criptografada = self.binario_para_texto(mensagem_binaria)
        mensagem_original = self.decifrar(mensagem_criptografada)
        return mensagem_original
