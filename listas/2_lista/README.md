1. Nossos olhos colapsam o mundo (3D) em imagens na retina, que pode ser considerada como uma superfície (2D). O cérebro tem então que reconstruir em (3D). A simulação deste processo em síntese de imagens, num computador, tem duas partes: transformação de __________________ (posição de câmera e orientação) e transformação de __________________ (reduz 3D para 2D). Ambas usam transformações ___________________ que formam a raiz da hierarquia de transformações.

2. O que voce entende por camera pin-hole? Qual o principal problema da camera pin-hole e como resolve-lo?

3. Qual a principal diferenca entre projeção ortográfica e projeção perspectiva? Sugestão: defina as duas.
   
4. Descreva detalhadamente o modelo (approach) mais popular para implementar a transformacao de visualizacao (frustum, viewing, look_from, look_at, vup, etc). Use desenhos graficos para ilustrar a sequencia de transformacoes e coloque as equações e matrizes dessas operações.
   
5. Uma câmera fotográfica digital com distância focal de 100 mm e ângulo de abertura de 90 graus em ambas as direções (vertical e horizontal) encontra-se no ponto (2,3,2), sistema MKS, direcionada (com sua lente apontando) para o ponto (2,2,0), orientada de modo que o eixo x da câmera esteja na horizontal. Dê o que se pede:
   
   - Qual a quantidade de pixels no plano imagem (dimensões da imagem), sabendo que cada pixel tem dimensão de 1x1 mm na imagem e que a janela de exibição guarda as mesmas proporções que o Frustum (toda a cena vista no Frustum cabe na imagem) ?

   - Sabendo que a origem do sistema de coordenadas da imagem (no monitor, seria a origem da janela de exibição) encontra-se no canto inferior esquerdo, como no OpenGL, quais as coordenadas de imagem (em pixels) dos vértices do triângulo formado pelos pontos (1,1,0), (3,1,0), (2,3,0) ? Faça um desenho gráfico (em escala) mostrando a imagem com o triângulo desenhado nela (2D). Obs: não desenhar partes do triângulo fora da imagem, se isto ocorrer.

6. Considerando uma câmera na origem do sistema de coordenadas (MKS), olhando para a direção (1, 1, 1), calcule o ponto de interseção (mais proximo do observador) do seu eixo visual com a esfera centrada em (4,2,2) e de raio igual a 2, ou seja, o ponto visível na esfera.