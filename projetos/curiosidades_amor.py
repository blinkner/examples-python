import numpy as np
import matplotlib.pyplot as plt

tecla = 1
print('\n')
for i in range(70):
    if i == 69:
        print('-')
        break
    print('-', end='')

print('Bem-vinda a um programinha feito especialmente para meu amorzinho!')
print('Aqui te responderei sobre curiosidades da nossa relação.')
for i in range(70):
    print('-', end='')

while tecla != 0:
    print('\n')
    print('[1] - Como e onde nos conhecemos?')
    print('[2] - O que eu sou seu?')
    print('[3] - Como eu te vejo?')
    print('[4] - O que mais desejo nesse mundo?')
    print('[5] - O que me fazem ficar todo bobo apaixonado vendo você fazer?')
    print('[0] - Sair')

    tecla = int(input('Qual opção você deseja? '))
    print('\n')

    if tecla == 1:
        print('[Expectativa] Nos conhecemos no instagram, essa bela mulher do nada curtiu minha foto e então a chamei para conversar, depois de muita troca de mensagem acabamos marcando de nos encontrar e não nos desgrudamos mais.')
        print('[Realidade] Nos conhecemos no tinder, a conversa era sempre interessante mas quando a chamei para sair você sumiu por muitos meses. Depois de um bom tempo você reapareceu curtindo minha foto no instagram no dia 24 de março de 2022, então eu a chamei para conversar e finalmente marcamos de nos encontrar na sua casa. Eu rodei a cidade para te ver, estava ansioso pra te conhecer pois eu gostava muito das nossas conversas até ali (claro que eu tinha um pouco de receio de você não gostar de mim). O encontro foi bom e então não nos desgrudamos mais. Eu fui me apaixonando por cada detalhe seu, cada centímetro do seu corpo e cada sonho que você tinha. Percebi que você era a pessoa perfeita pra mim, quem eu ansiava profundamente encontrar, alguém que realmente me entendia e me valorizava. E então, aqui estou, louco pela mulher que tenho ao meu lado.')
    elif tecla == 2:
        print('Seu mu mu para sempre!!!')
    elif tecla == 3:
        print('Te vejo como a mulher mais incrível e linda desse mundo, maravilhosa em cada mínimo detalhe, alguém que admiro e confio profundamente. Te vejo como a mulher e a pessoa perfeita para compartilhar a vida, mais do que eu poderia imaginar para mim mesmo. Você é meu sonho, minha paixão, meu sorriso, minha paz. Você é extremamente forte, que eu sei que enfrentaria o mundo pelas coisas que acredita, eu amo e valorizo isso. Você é a dona do meu coração e o amor da minha vida todinha.')
    elif tecla == 4:
        print('Você, sua felicidade e conseguir proporcionar a vida que você merece.')
    elif tecla == 5:
        print('- Você se maquiando;')
        print('- Você trocando de roupa;')
        print('- Você brincando com o paçoquinha;')
        print('- Você usando suas habilidades de enfermeirinha pra me furar;')
        print('- Você assistindo e gostando das coisinhas que eu recomendo (One Piece, Diários de um Vampiro, Sobrenatural...);')
        print('- Você cozinhando;')
        print('- Você me enchendo de beijinhos;')
        print('- Você sendo safada;')
        print('- Você me explicando coisinhas de enfermagem que eu não entendo nada;')
        print('- Você respirando;')
        print('- Você simplesmente sendo você S2.')
    elif tecla == 0:
        break
    else:
        print('Opção inválida!')

x = np.arange(-2, 2, 0.001)
p1 = (1 - (abs(x) - 1)**2)**(0.5)
p2 = -2.5 * (1 - (abs(x)/2)**(0.5))**(0.5)

plt.figure()
plt.title('EU TE AMO')
plt.plot(x, p1, 'r')
plt.plot(x, p2, 'r')
plt.ylim((-3, 2))
plt.xlim((-3, 3))
plt.grid()
plt.show()