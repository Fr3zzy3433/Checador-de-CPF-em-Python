import os
#os.system('cls')

cpf_soma = []
recomeco = True
cpf_multi2 = 0
while True:


    cpf = (input('Digite seu cpf, somente números: '))
    if len(cpf) >11 or len(cpf) < 11:
        print('Digite um cpf Válido!')
        continue
        
    elif cpf.isdigit() == False:
        print('Digite somente números')
        continue

    else:
        cpf_tratado = [int(x) for x in cpf]
        cpf_tratado2 = [int(x) for x in cpf]
    
    cpf_somente9num = cpf_tratado2.pop(-1)
    cpf_somente9num = cpf_tratado2.pop(-1)

    cpf_multi = (cpf_tratado[0]*10) + (cpf_tratado[1]*9) + (cpf_tratado[2]*8) + (cpf_tratado[3]*7) + (cpf_tratado[4]*6) + (cpf_tratado[5]*5) + (cpf_tratado[6]*4) + (cpf_tratado[7]*3) + (cpf_tratado[8]*2)
    #cpf_soma = sum(cpf_multi)
    cpf_divisao = cpf_multi%11
    cpf_checar = 11-cpf_divisao
    

    if cpf_tratado[9] == cpf_checar:
        cpf_multi2 = (cpf_tratado[0]*11) + (cpf_tratado[1]*10) + (cpf_tratado[2]*9) + (cpf_tratado[3]*8) + (cpf_tratado[4]*7) + (cpf_tratado[5]*6) + (cpf_tratado[6]*5) + (cpf_tratado[7]*4) + (cpf_tratado[8]*3) + (cpf_tratado[9]*2)
    
    cpf_final = cpf_multi2%11
    cpf_ultimo = 11 - cpf_final

    if cpf_tratado[9] == cpf_checar and cpf_tratado[10] == cpf_ultimo:
        os.system('cls')
        print('Seu CPF é valido')
        recomeco = input('Deseja checar outro CPF? [y/n]: ')
        youn = recomeco.lower()
        if youn == 'y':
            continue
        else:
            print('Até a próxima')
            break

    else:
        print('Seu CPF não é valido') 
        recomeco = input('Deseja checar outro CPF? [y/n]: ')
        youn = recomeco.lower()
        if youn == 'y':
            continue
        else:
            print('Até a próxima')
            break


    
    

