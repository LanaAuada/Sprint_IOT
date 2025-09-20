# README -- Detector Facial com OpenCV

Julia Amorim - RM99609
Lana Leite - RM551143
Matheus Cavasini - RM97722

## Objetivo

Este projeto tem como objetivo desenvolver uma aplicação local
(desktop/notebook) que realize detecção facial em tempo real utilizando
a webcam.\
A aplicação utiliza a biblioteca OpenCV e o classificador Haar Cascade
para identificar rostos, permitindo o ajuste de parâmetros que
influenciam diretamente a qualidade da detecção.

------------------------------------------------------------------------

## Dependências

É necessário ter o Python instalado em sua máquina.\
As bibliotecas necessárias podem ser instaladas com o seguinte comando:

``` bash
pip install opencv-python
```

Além disso, é necessário o arquivo do classificador Haar Cascade:

-   **haarcascade_frontalface_default.xml**\
    Disponível no repositório oficial do OpenCV:\
    [Download
    XML](https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml)

Coloque o arquivo na mesma pasta do script `detector_faces.py`.

------------------------------------------------------------------------

## Execução

1.  Baixe ou clone o repositório.\
2.  Certifique-se de que o arquivo `haarcascade_frontalface_default.xml`
    está no mesmo diretório do script.\
3.  Execute o código pelo terminal:

``` bash
python detector_faces.py
```

4.  Uma janela será aberta exibindo o vídeo da webcam com a detecção de
    rostos em tempo real.\
5.  Para encerrar a execução, pressione a tecla **q**.

------------------------------------------------------------------------

## Parâmetros Ajustáveis

Na janela principal, existem controles deslizantes (trackbars) que
permitem alterar os parâmetros em tempo real:

-   **Scale Factor (Scale x100)**\
    Define o quanto a imagem é reduzida a cada escala de detecção.\
    Valores menores (ex.: 1.05) aumentam a precisão, mas tornam a
    execução mais lenta.\
    Valores maiores (ex.: 1.3) aumentam a velocidade, mas podem deixar
    de detectar rostos.

-   **Min Neighbors**\
    Define o número mínimo de vizinhos necessários para validar uma
    detecção.\
    Valores baixos tornam a detecção mais sensível, mas podem gerar
    falsos positivos.\
    Valores altos reduzem falsos positivos, mas podem deixar de detectar
    alguns rostos.

-   **Min Size**\
    Define o tamanho mínimo do rosto a ser considerado.\
    Valores baixos permitem detectar rostos menores ou mais distantes.\
    Valores altos restringem a detecção apenas a rostos maiores ou
    próximos.

------------------------------------------------------------------------

## Limitações

-   O método Haar Cascade pode falhar em ambientes com baixa iluminação
    ou quando o rosto está inclinado.\
-   Esta aplicação realiza apenas a detecção de rostos, não a
    identificação de pessoas.

------------------------------------------------------------------------

## Próximos Passos

-   Implementar detecção mais robusta utilizando bibliotecas como
    MediaPipe ou dlib.\
-   Adicionar reconhecimento facial para identificar usuários.\
-   Desenvolver uma interface gráfica para facilitar o uso da aplicação.

------------------------------------------------------------------------

## Nota Ética sobre Uso de Dados Faciais

O uso de tecnologias de detecção e reconhecimento facial deve ser feito
de forma ética e responsável.\
É importante considerar aspectos como:

-   **Privacidade**: dados biométricos são sensíveis e não devem ser
    coletados ou armazenados sem consentimento explícito do usuário.\
-   **Finalidade**: a aplicação apresentada tem caráter apenas acadêmico
    e demonstrativo. Não deve ser utilizada para vigilância ou
    monitoramento sem autorização.\
-   **Segurança**: qualquer armazenamento ou processamento de imagens
    faciais em projetos futuros deve adotar práticas de proteção de
    dados.\
-   **Viés e justiça**: algoritmos de visão computacional podem
    apresentar vieses dependendo do conjunto de treinamento utilizado,
    devendo ser avaliados criticamente antes de aplicação prática.
