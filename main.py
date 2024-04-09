import os

from realce import Realce
from ruidos import Ruidos
import cv2
def main():

    #exercicio4
    for imagem in os.listdir("./images4"):
        img = cv2.imread('./images4/'+imagem, cv2.IMREAD_GRAYSCALE)
        ruido = Ruidos(img)
        ruido.plotHistograma()
        img_gaussian = ruido.plotGaussian()
        err_max =ruido.erromaximo(img_gaussian)
        err_md_abs = ruido.errmomedioabsoluto(img_gaussian)
        err_md_sqr= ruido.erromedioquadratico(img_gaussian)
        raiz_err_md_sq =ruido.raizdoerromedioquadratico(img_gaussian)
        err_md_sqr_norm = ruido.erromedioquadraticonormalizado(img_gaussian)
        jaccard = ruido.coeficientedeJaccard(img_gaussian)


        print("ERRO Maximo: ",err_max)
        print("ERRO Medio Absoluto: ",err_md_abs)
        print("ERRO Medio quadratico: ",err_md_sqr)
        print("Raizs Erro medio quadratico: ",raiz_err_md_sq)
        print("Erro Medio Quadratico normalizado: ",err_md_sqr_norm)
        print("Jaccard: ", jaccard)

        print("è possivel observar que nos casos do erro maximo a raiz do erro medio quadratico, quanto maior o numero maior a diferença entre as imagens"
              "e no caso do coeficiente de jaccard, quanto menos o numero (mais proximo de 0), mmaior a diferença entre as imagens")
        print("A metrica que permite evidenciar melhor é o coeficiente de jaccar,"
              "pois como ele avalia pixel a pixel e  caso seja igual ele o considera como válido (1),"
              "isso implica que se uma imagem, após aplicação de ruido não preservar  nenhum pixel original,"
              "significa que a imagem após a aplicação de ruido tornou-se uma imagem totalmente diferente ")



    #EXERCICIO 7 Equalização de IMAGEM
    for imagem in os.listdir("./images"):
        img = cv2.imread('./images/'+imagem, cv2.IMREAD_GRAYSCALE)
        realce = Realce(img, imagem)
        realce.show()
        realce.plotHistograma()
        realce.plotHistogramaEqualizado()
        realce.equalizeImg()


    #exercicio9
    for imagem in os.listdir("./images4"):
        img = cv2.imread('./images4/'+imagem, cv2.IMREAD_GRAYSCALE)
        ruido = Ruidos(img)
        ruido.plotHistograma()
        im_gausss =ruido.plotGaussian()
        realce = Realce(im_gausss, imagem)
        #realce.show()
        #realce.negativo()
        realce.correcaoGamma(0.04, 1)
        realce.correcaoGamma(0.4, 1)
        realce.correcaoGamma(2.5, 1)
        realce.correcaoGamma(10, 1)
        #realce.correcaoGamma(25, 1)
        #realce.correcaoGamma(100, 1)

    print("realçar com a correção gamma  permitiu melhorar a qualidade da imagem com o valor de gamma igual a 10, utilização de realce para corrigir uma imagem degradada depende do tipo de realce e quais caraceristicas está sendo buscada para realce.")

main()