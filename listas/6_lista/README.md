1. Defina o problema de visibilidade.

2. Quais são os 4 algoritmos básicos de visibilidade? Coloque o pseudo-código de cada um deles (são 4).

3. Explique em detalhes as vantagens e desvantagens de 3 dos algoritmos de visibilidade.

4. Qual dos algoritmos de visibilidade voce usaria se tivesse apenas um objeto, modelado com muitas faces triangulares a ser visualizado? Explique o motivo.

5. Qual o princípio básico do "forward ray-tracing"? Explique.

6. Qual a diferença básica entre o "Forward Ray Tracing" e o "Backward Ray Tracing" (qual o principal problema do primeiro método, resolvido pelo segundo) ?

7. Explique a ideia básica do "ray-tracing" recursivo, incluindo quais os tipos de raios recursivos a se considerar, descrevendo sucintamente cada um deles

8. (Desafio-bonus) Uma câmera com distância focal de 100 mm, cujo plano imagem é formado por 100x100 pixels com dimensões de 1x1mm cada um, encontra-se na origem do sistema de coordenadas com sua objetiva (eixo focal) apontando para o eixo Z do sistema. Dê o que se pede:
Calcule as coordenadas do ponto visível (ou ponto de interseção) na esfera de raio 2 que se encontra centrada em (-1,0,4), cuja projeção na imagem é o pixel (50,50), sabendo que a origem do sistema de imagem é como no OpenGL (canto inferior esquerdo).
Use a equação de iluminação vista em sala para determinar a contribuição do ponto acima na esfera para o pixel correspondente na imagem (50,50). Sabe-se que a posição da luz é (1,1,1), que ela é pontual e monocromática de intensidade luminosa 200. Assuma que o coeficiente de reflexão ambiente é 0,5, que a intensidade da luz ambiente é 100, que o espalhamento da reflex&atilode;o especular é 1, desconsidere atenuação e arbitre os outros parâmetros da equação de iluminação de forma que a superfície seja 60% difusa e 40% especular.
Determine os vetores (em coordenadas de mundo - MKS) que representam as direções dos raios para o ray-tracing recursivo.
