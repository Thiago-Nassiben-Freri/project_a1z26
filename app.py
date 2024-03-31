import functions

def cryptographerUX(): 
    while True: 
        var_choice = input('Deseja utilizar o criptografador de A1Z26? [S/N]: ')
        try: 
            if var_choice.upper() == 'S': 
                var_texto_plano = input('Digite o texto (plano): ')
                var_texto_criptografado = functions.cryptographerA1Z26(var_texto_plano)

                print(f'O texto "{var_texto_plano}" foi criptografado: {var_texto_criptografado}')
            elif var_choice.upper() == 'N': 
                functions.exit()
                break
        except ValueError: 
            print("\033[91m Erro: Valor registrado inválido! \033[0m")

if __name__ == '__main__': 
    cryptographerUX()