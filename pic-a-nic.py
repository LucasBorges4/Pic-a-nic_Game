num_players = int(input("Quantos vão brincar com a gente?"))
vetor = []
for a in range(num_players):
        nome = str(input("Qual seu nome amigo?"))
        vetor.append(nome)

while True:
    
    vez = 0
    print(f"O que voce quer levar ao picnic {vetor[vez % num_players]} ?")
    coisa = str(input())
    print(f"Eu quero levar ao picnic um {coisa}.")

    if coisa[0] == vetor[vez % num_players][0]:
        print("Você pode levar ao picnic! :)")
    else:
        print("Sinto muito, mas você não pode levar ao picnic. :(")
    
    vez+=1
    


    