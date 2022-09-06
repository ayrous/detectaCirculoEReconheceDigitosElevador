# Reconhecimento de Círculos e Dígitos em Uma Imagem com text to speech
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
## Para executar este programa apenas e testar suas entradas e saídas:
	- $ python3 getVoice.py

## HoughCircles.py
