import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os

# Caminho relativo para o arquivo haarcascade_frontalface_default.xml
cascade_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')

# Carregar o classificador Haar Cascade
cascade = cv2.CascadeClassifier(cascade_path)

# Verificar se o classificador foi carregado corretamente
if cascade.empty():
    raise IOError("Unable to load the cascade classifier xml file")

# Inicialização da câmera
cam = cv2.VideoCapture(0)

# Função para redimensionar a imagem mantendo a proporção
def resize_image(image, width=None, height=None):
    # Obtém as dimensões originais da imagem
    original_width, original_height = image.size
    
    # Se tanto largura quanto altura forem especificadas, redimensiona mantendo a proporção
    if width and height:
        if original_width > original_height:
            ratio = width / float(original_width)
            height = int(ratio * original_height)
        else:
            ratio = height / float(original_height)
            width = int(ratio * original_width)
    # Se apenas a largura for especificada, calcula a altura proporcionalmente
    elif width:
        ratio = width / float(original_width)
        height = int(ratio * original_height)
    # Se apenas a altura for especificada, calcula a largura proporcionalmente
    elif height:
        ratio = height / float(original_height)
        width = int(ratio * original_width)
    
    # Retorna a imagem redimensionada
    return image.resize((width, height))

# Função para atualizar o frame da câmera
def update_frame():
    _, img = cam.read()  # Lê o frame da câmera
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza
    faces = cascade.detectMultiScale(grayImg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))  # Detecta faces

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Desenha retângulo ao redor da face

    # Converte imagem OpenCV para formato que Tkinter pode exibir
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    
    # Redimensiona a imagem para exibir em uma resolução maior (exemplo: dobrando as dimensões)
    img = resize_image(img, width=img.width * 2, height=img.height * 2)
    
    img = ImageTk.PhotoImage(image=img)

    # Atualiza o label da imagem na interface
    panel.imgtk = img
    panel.config(image=img)
    panel.after(10, update_frame)  # Atualiza a cada 10 milissegundos

# Criação da janela principal
root = tk.Tk()
root.title("Face Detection")

# Cria um label na janela para exibir a imagem
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# Chama a função para atualizar o frame da câmera
update_frame()

# Função para fechar a janela quando pressionar 'q' ou 'Q'
def close(event):
    if event.char == 'q' or event.char == 'Q':
        root.destroy()

root.bind('<Key>', close)

# Inicia o loop principal da interface gráfica
root.mainloop()

# Libera a câmera e fecha todas as janelas abertas do OpenCV
cam.release()
cv2.destroyAllWindows()
