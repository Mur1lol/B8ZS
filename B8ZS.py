class B8ZS:
    def __init__(self):
        pass

    ## Codifica para B8ZS
    def encode(self, sinal):
        sinal_ami = self.__ami(sinal) # codificação AMI
        return self.__violation_bipolar(sinal_ami)

    ## Decodifica de B8ZS
    def decode(self, sinal_digital):
        sinal_ami = self.__undo_violation(sinal_digital)
        return self.__undo_ami(sinal_ami)

    ## Técnica de codificação de clock síncrono que utiliza pulsos bipolares para representar o lógico 1.
    @staticmethod
    def __ami(bits):
        up = True
        sinal_digital = []
        for bit in bits:
            if bit == 1:
                if up:
                    sinal_digital.append(1)
                else:
                    sinal_digital.append(2)
                up = not up
            else:
                sinal_digital.append(0)
        return sinal_digital

    ## Substitui 8 zeros consecutivos por uma violação dupla
    @staticmethod
    def __violation_bipolar(sinal_digital):
        
        violacao = '00000000'
        sinal = ''.join(str(i) for i in sinal_digital)

        while violacao in sinal:
            i = sinal.index(violacao)
            if sinal[i - 1] == '1':
                resposta = '00012021' # 000VB0VB
            else:
                resposta = '00021012' # 000VB0VB
            
            sinal = sinal.replace(violacao, resposta, 1)

        let_to_num = {'0': 0, '1': 1, '2': -1}
        novo_sinal = [let_to_num[i] for i in sinal]
        
        return novo_sinal

    ## Substitui a violação por 8 zeros consecutivos
    @staticmethod
    def __undo_violation(sinal_digital):
        sinal = [2 if x==-1 else x for x in sinal_digital]
        sinal = ''.join(str(i) for i in sinal)
        
        sinal = sinal.replace('00012021', '00000000')
        sinal = sinal.replace('00021012', '00000000')

        let_to_num = {'0': 0, '1': 1, '2': -1}
        
        return [let_to_num[i] for i in sinal]

    @staticmethod
    def __undo_ami(sinal_ami):
        return [1 if x==-1 else x for x in sinal_ami]

    ## Transforma o formato do sinal de lista para string, substituindo -1's por 2's
    @staticmethod
    def signal_to_string(sinal):
        sinal = [2 if x==-1 else x for x in sinal]
        sinal_string = ''.join([str(item) for item in sinal])
        return sinal_string

    ## Transforma o formato do sinal de string para lista, substituindo 2's por -1's
    @staticmethod
    def string_to_signal(palavra):
        let_to_num = {'0': 0, '1': 1, '2': -1} 
        return [let_to_num[i] for i in palavra]
