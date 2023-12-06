class CifraDeCesar:
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento
        self.alfabeto = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'

    def cifrar(self, texto):
        texto_cifrado = self.deslocar_texto(texto, self.deslocamento)
        return texto_cifrado, self.texto_para_binario(texto_cifrado)

    def decifrar(self, texto_cifrado):
        texto_decifrado = self.deslocar_texto(texto_cifrado, -self.deslocamento)
        return texto_decifrado, self.texto_para_binario(texto_decifrado)

    def deslocar_texto(self, texto, deslocamento):
        texto_deslocado = ''
        for char in texto:
            if char in self.alfabeto:
                maiuscula = char.isupper()
                texto_deslocado += self.deslocar_letra(char, deslocamento, maiuscula)
            else:
                texto_deslocado += char
        return texto_deslocado

    def deslocar_letra(self, char, deslocamento, maiuscula):
        base = self.alfabeto[0].upper() if maiuscula else self.alfabeto[0].lower()
        indice = (self.alfabeto.index(char) + deslocamento) % len(self.alfabeto)
        return self.alfabeto[indice]

    @staticmethod
    def texto_para_binario(texto):
        return ''.join(format(ord(char), '08b') for char in texto)

    @staticmethod
    def binario_para_texto(binario):
        return ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))

# Exemplo de uso:
texto_original = "Meu nome é Murilo e minha mãe é a Mônica"
deslocamento_cesar = 3

cesar_cipher = CifraDeCesar(deslocamento_cesar)

# Criptografia
texto_cifrado, texto_cifrado_binario = cesar_cipher.cifrar(texto_original)
print(f"Texto Original: {texto_original}")
print(f"Texto Criptografado: {texto_cifrado}")
print(f"Texto Criptografado em Binário: {texto_cifrado_binario}")

# Descriptografia
texto_decifrado, texto_decifrado_binario = cesar_cipher.decifrar(texto_cifrado)
print(f"Texto Descriptografado: {texto_decifrado}")
print(f"Texto Descriptografado em Binário: {texto_decifrado_binario}")

# Convertendo de binário para texto
texto_decifrado_do_binario = cesar_cipher.binario_para_texto(texto_decifrado_binario)
print(f"Texto Descriptografado do Binário: {texto_decifrado_do_binario}")
