# Projeto de Detecção de Faces e Olhos com OpenCV

## Descrição
Este projeto utiliza o OpenCV para detectar faces e olhos em imagens e vídeos em tempo real. A detecção é feita usando classificadores em cascata treinados com algoritmos Haar.

## Pacotes para Instalação
Optamos pela instalação do OpenCV-Python no Ubuntu devido à praticidade e à versão compacta de "Pre-Built binaries" disponíveis para essa linguagem.

**Nota:** Os repositórios podem não conter a versão mais recente do OpenCV. Por exemplo, no momento da redação deste tutorial, o repositório apt contém a versão 2.4.8, enquanto a versão mais recente do OpenCV é 3.x.

Para instruções sobre como proceder em outros sistemas operacionais, consulte o [tutorial oficial do OpenCV](https://docs.opencv.org/4.x/da/df6/tutorial_py_table_of_contents_setup.html).

### Instalação no Ubuntu
Para instalar no Ubuntu, siga o tutorial: [Configuração no Ubuntu](https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html).

## Arquivos Necessários
Certifique-se de que os seguintes arquivos XML de cascata estejam no diretório do projeto:
- `haarcascade_frontalface_default.xml`
- `haarcascade_frontalface_alt.xml`
- `haarcascade_eye_tree_eyeglasses.xml`

Se esses arquivos não estiverem no diretório do repositório, encontre-os e adicione o caminho completo nos parâmetros requisitados no código.

## face_and_eye_detection.py
Este script detecta faces e olhos em tempo real usando a câmera do computador. Para sair da tela, pressione a tecla "ESC".

### Exemplo de Uso
Este exemplo é adaptado do tutorial de detecção de objetos do OpenCV: [Cascade Classifier Tutorial](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html).

![Exemplo de Detecção de Faces e Olhos](https://docs.opencv.org/3.4/Cascade_Classifier_Tutorial_Result_Haar.jpg)

## face_detection.py
Este script detecta faces em tempo real usando a câmera do computador.

### Exemplo de Uso
Este exemplo é adaptado de [PyImageSearch](https://pyimagesearch.com/2021/04/05/opencv-face-detection-with-haar-cascades/).

![Exemplo de Detecção de Faces](https://b2633864.smushcdn.com/2633864/wp-content/uploads/2021/02/opencv_haar_cascade_face_detection_output02.jpg?lossy=2&strip=1&webp=1)

## Links importantes para aprender ainda mais sobre OpenCV
### Oficial
  [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
### Extra
  [geeksforgeeks](https://www.geeksforgeeks.org/opencv-python-tutorial/)
  e [pythonprogramming.net](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

## Contribua com a comunidade [OpenCV](https://github.com/opencv/opencv)
"Since OpenCV is an open source initiative, all are welcome to make contributions to the library, documentation, and tutorials."

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
