import cv2

#Carrega o classificador Haar Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Abre a webcam
cap = cv2.VideoCapture(0)

#Cria janela
cv2.namedWindow("Detecção Facial")

#Função vazia para os trackbars
def nothing(x):
    pass

#Cria trackbars para ajustar parâmetros
cv2.createTrackbar("Scale x100", "Detecção Facial", 110, 200, nothing)   # 110 => 1.10 | precisão da busca
cv2.createTrackbar("MinNeighbors", "Detecção Facial", 5, 20, nothing)    # padrão 5 | aceita a detecção e equilibra
cv2.createTrackbar("MinSize", "Detecção Facial", 30, 200, nothing)       # 30 px |  tamanho do rosto

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Lê valores dos trackbars
    scale = cv2.getTrackbarPos("Scale x100", "Detecção Facial") / 100.0
    neighbors = cv2.getTrackbarPos("MinNeighbors", "Detecção Facial")
    min_size = cv2.getTrackbarPos("MinSize", "Detecção Facial")

    #Detecta rostos
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=max(scale, 1.01),
        minNeighbors=max(neighbors, 1),
        minSize=(min_size, min_size)
    )

    #Desenha retângulos nos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #Mostra parâmetros na tela
    cv2.putText(frame, f"scale={scale:.2f} neighbors={neighbors} minSize={min_size}", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    #Exibe a imagem
    cv2.imshow("Detecção Facial", frame)

    #Tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
