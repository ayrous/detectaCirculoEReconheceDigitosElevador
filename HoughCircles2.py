#!/usr/bin/env python3
from unittest import result
import cv2
import numpy as np
from keras.models import load_model
import getVoice
import time

def image_reader():
    src_img = cv2.imread('imagens/elevador_numdois.jpeg')
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray,(5,5),0)

    return src_img, blur_img

def circles_detect(src_img, blur_img):
    circles_img = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1,150,
                                param1=50,param2=30,minRadius=150,maxRadius=170)  
    circles_img = np.array(circles_img).astype(float)
    circles_img = np.uint16(np.around(circles_img))
    print(circles_img)
    #sorted(circles_img , key=lambda k: [k[1], k[0]])
    #n = 9
    for (x, y, raio) in circles_img[0,:]:
        cv2.circle(src_img,(x, y), raio,(0,255,0),2)
        #n -= 1
        #number = str(n)
        #cv2.putText(src_img, number, (x, y), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 255, 0), 4)
        

    return src_img, circles_img

def crop_button(circles_list, n):
    x = circles_list[0][n][0]
    y = circles_list[0][n][1]
    raio = circles_list[0][n][2]
    distancia = raio/12   #Relação em pixel/mm do tamanho do botão
    box_size = (100,150)
    maiorx = x - distancia*30 + box_size[0]
    menorx = x - distancia*30 - box_size[0]
    maiory = y + box_size[1] - 40
    menory = y - box_size[1] - 40
    cv2.rectangle(src_img, (int(menorx), int(menory)), (int(maiorx), int(maiory)), (0, 128, 255), 4)
    img_cortada = blur_img[int(menory):int(maiory), int(menorx):int(maiorx)]
    #edges = cv2.Laplacian(img_cortada,cv2.CV_64F)
    #cv2.imshow("cortado", img_cortada)
    return img_cortada, x, y

def show_image(image):
    image = cv2.resize(image, (540, 990))
    cv2.imshow('Detected Circles',image)

def prediction(frame_cortado, model):
    
    img = cv2.resize(frame_cortado, (28,28))
    img = img/255
    img = img.reshape(1,28,28,1)
    predict = model.predict(img)

    probabilidade = np.amax(predict)
    class_index = np.argmax(model.predict(img),axis=1)
    resultado = class_index[0]

    if probabilidade < 0.9:
        resultado = 0
        probabilidade = 0
    return resultado,probabilidade


if __name__ == '__main__':
    key = 0
    #numProcura = 5
    numProcura = getVoice.main()
    src_img, blur_img = image_reader()
    marqued_img, circles_list= circles_detect(src_img, blur_img)
    model = load_model('model/digits.h5')
    resultados = []
    probabilidades = []

    while(True): 

        button, x, y = crop_button(circles_list, key)
        resultado, probabilidade = prediction(button, model)
        resultados.append(resultado)
        probabilidades.append(probabilidade)
        
        cv2.putText(marqued_img, f"Predicao: {resultados[key]}", (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,0,255), 4,cv2.LINE_AA)
        cv2.putText(marqued_img, f"Probabilidade: {probabilidades[key]}", (40, 250), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,0,255),4, cv2.LINE_AA)
        
        if resultado == numProcura and probabilidade>= 0.999:
            getVoice.speak("Vamos para o "+ str(numProcura))
            cv2.putText(marqued_img, f"Coordenadas x: {x}", (40, 250), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,0,255),4, cv2.LINE_AA)
            cv2.putText(marqued_img, f"Coordenadas y: {y}", (40, 250), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,0,255),4, cv2.LINE_AA)
            time.sleep(10)
            break
        cv2.imshow("cortado 0", button)

        show_image(marqued_img)

        if cv2.waitKey(1) & 0XFF == ord('p'):
                #getVoice.speak("Até mais!")
#                break
            key+=1
            if key > 9 or key <=0:
                getVoice.speak("Até mais!")
                break

    #cv2.waitKey(0)
    cv2.destroyAllWindows()