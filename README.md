# Reconhecimento de Círculos e Dígitos em uma Imagem com Input de Voz
Detecção de círculos e reconhecimento de dígitos de um painel de elevador com input e output de voz.

### Este projeto tem como objetivo macro auxiliar pessoas de algum grau de deficiência visual a conseguirem utilizar o elevador de forma mais fácil ao detectar os círculos de uma imagem e realizar o reconhecimento dos números de 0-9 ao lado dos botões circulares de um painel de elevador.

## Bibliotecas necessárias:
	- OpenCV 4.6.0
    - Numpy 1.23.0
    - Keras 2.9.0
    - Time
    - Speech Recognition 3.8.1
    - Gtts 2.2.4
    - Playsound
    - Nltk 3.7
    
### Neste programa há uso do modelo 'digits.h5', que será carregado posteriormente pela função 'load_model' da biblioteca Keras.

## getVoice.py
### Este programa tem como objetivo realizar as seguintes etapas:
  - Executar text-to-speech para perguntar a pessoa qual andar ela pretende ir
  - Executar speech-to-text ao receber uma entrada de voz
  - Reconhecer as palavras ditas e coloca-las em uma lista
  - Percorrer a lista procurando por números de andares, caso contrário pedir novamente que seja dito o andar onde a pessoa deseja seguir
### Para executar apenas este programa e testar suas entradas e saídas:
	$ python3 getVoice.py

## HoughCircles.py
### Este programa tem como objetivo realizar as seguintes etapas:
  - Chamar o programa getVoice.py e armazenar o número pretendido em uma variável
  - Ler a imagem e aplica filtros nela (escala de cinza e blur)
  - Detectar os círculos na imagem utilizando da função HoughCircles da biblioteca OpenCV, obtendo as coordenadas x,y em pixels e o raio dos círculos encontrados e armazenando em uma lista
  - Carregar o modelo 'digits.h5' com a biblioteca Keras
  - Aplicar cortes na imagem nos locais próximos onde estão os botões (dado o x,y e raio anteriores), com objetivo de encontrar os números relacionados àquele botão circular do painel e retornar a imagem recortada com filtro de blur
  - Desenhar um retângulo ao redor de cada caractere ao lado dos círculos detectados
  - A partir de cada imagem recortada, analisar e aplicar a predição de dígitos do modelo carregado, após redimensiona-la.

Caso a probabilidade seja superior ou igual a 0.999 e o resultado seja o número do andar dito pela pessoa no início, o programa é encerrado retornando as coordenadas do botão próximo ao dígito localizado.
### Para executar este programa:
	$ python3 HoushCircles2.py
O reconhecimento de dígitos é feito um por vez, dependendo do número de círculos detectados na imagem. É precido apertar a tecla 'q' para que o programa troque o corte para o próximo ao botão circular e aplque a predição.

## Extra
 Dependendo da sua imagem e do seu objetivo pode ser necessário alterar os parâmetros do HoughCircle, dentro da função circles_detect do programa HoughCircles2.py.

Para uso da câmera da webcam, é recomendado a inatalação do aplicativo IP Webcam em seu celular, colocando em seu código o endpoint IPV4 fornecido após iniciar o servidor.
