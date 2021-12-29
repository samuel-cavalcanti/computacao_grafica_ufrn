%% Encontrando dimensão da janela

% encontra as dimensões da imagem
d = 100*10^-3
fov = 90
A = 2*d*tand(fov/2)

pixel_size_x = 10^-3
pixel_size_y = 10^-3

janela_x = A/pixel_size_x
janela_y = A/pixel_size_y

% no plano imagem 0.2 x 0.2; na janela 200 x 200 (40,000 pixels)
px_pi = [-0.1 -0.1 0.1 0.1 -0.1]
py_pi = [0.1 -0.1 -0.1 0.1 0.1]
pz_pi = [0.1 0.1 0.1 0.1 0.1]

subplot(1,2,1);
plot(px_pi, py_pi)
title('Plano imagem')
axis([-1 1 -1 1])
grid

subplot(1,2,2);
px_j = [0 200 200 0 0]
py_j = [0 0 200 200 0]

plot(px_j, py_j)
title('Janela')
axis([-300 300 -300 300])
grid

%% Cena

p1 = [1 1 0 1]
p2 = [3 1 0 1]
p3 = [2 3 0 1]

lookat = [2 2 0 1]
lookfrom = [2 3 2 1]

figure

hold on;
plot3([p1(1) p2(1) p3(1) p1(1)], [p1(2) p2(2) p3(2) p1(2)], [p1(3) p2(3) p3(3) p1(3)], '-o','Color','r','MarkerSize',10)
plot3(lookfrom(1), lookfrom(2), lookfrom(3), '-o','Color','b','MarkerSize',14)
plot3([lookfrom(1) lookat(1)], [lookfrom(2) lookat(2)], [lookfrom(3) lookat(3)], 'k')
grid
axis([0 4 0 4 0 3])
xlabel('x') 
ylabel('y') 
zlabel('z')


%% Transformação de visualização

% calculando a transformação de visualização

Transl_cam = [1 0 0 -lookfrom(1);
              0 1 0 -lookfrom(2);
              0 0 1 -lookfrom(3);
              0 0 0       1]
          
% encontrar v
v = lookat(1:3) - lookfrom(1:3)
% normaliza v
v = v/norm(v)

z_can = [0 0 1]

% encontrar matriz de rotação para ajustar z de camera com z de mundo
cross_a_z = cross(v,z_can)

% eixo de rotação
a  = cross_a_z/norm(cross_a_z)

% angulo de rotação
theta = acosd(dot(v,z_can))

x = a(1);
y = a(2);
z = a(3);

% matriz de rotação para alinhar o eixo z da camera e do mundo
R_cam_z = [cosd(theta)+(1-cosd(theta))*x^2      (1-cosd(theta))*x*y-(sind(theta))*z  (1-cosd(theta))*x*z+(sind(theta))*y  0;
           (1-cosd(theta))*y*x+(sind(theta))*z  cosd(theta)+(1-cosd(theta))*y^2      (1-cosd(theta))*y*z-(sind(theta))*x  0;
           (1-cosd(theta))*x*z-(sind(theta))*y  (1-cosd(theta))*z*y+(sind(theta))*x  cosd(theta)+(1-cosd(theta))*z^2      0;        
                          0                                        0                                    0                 1
      ]
  
% T_cam (passa os pontos de coordenadas de mundo para coordenadas de camera)
T_cam = R_cam_z * Transl_cam

% coordenadas dos pontos em relação ao referencial de camera
p1_cam = T_cam*p1'
p2_cam = T_cam*p2'
p3_cam = T_cam*p3'
lookfrom_cam = T_cam*lookfrom'
lookat_cam = T_cam*lookat'

figure

hold on;

plot3(px_pi, py_pi, pz_pi)
plot3([p1_cam(1) p2_cam(1) p3_cam(1) p1_cam(1)], [p1_cam(2) p2_cam(2) p3_cam(2) p1_cam(2)], [p1_cam(3) p2_cam(3) p3_cam(3) p1_cam(3)], '-o','Color','r','MarkerSize',10)

plot3(lookfrom_cam(1), lookfrom_cam(2), lookfrom_cam(3), '-o','Color','b','MarkerSize',14)
plot3([lookfrom_cam(1) lookat_cam(1)], [lookfrom_cam(2) lookat_cam(2)], [lookfrom_cam(3) lookat_cam(3)], 'k')
grid
xlabel('x') 
ylabel('y') 
zlabel('z') 

%% transformação de projeção

T_per = [d 0 0 0;
         0 d 0 0;
         0 0 d 0;
         0 0 1 0]
     
% calcula a matriz de visualização e projeção     
T_vis_proj = T_per*T_cam

% coordenadas dos pontos no plano imagem
p1_pp = T_vis_proj*p1'
p2_pp = T_vis_proj*p2'
p3_pp = T_vis_proj*p3'
lookfrom_pp = T_cam*lookfrom'
lookat_pp = T_cam*lookat'

figure
hold on;

plot3(px_pi, py_pi, pz_pi)
plot3([p1_pp(1) p2_pp(1) p3_pp(1) p1_pp(1)], [p1_pp(2) p2_pp(2) p3_pp(2) p1_pp(2)], [p1_pp(3) p2_pp(3) p3_pp(3) p1_pp(3)], '-o','Color','r','MarkerSize',10)

plot3(lookfrom_pp(1), lookfrom_pp(2), lookfrom_pp(3), '-o','Color','b','MarkerSize',14)
plot3([lookfrom_pp(1) lookat_pp(1)], [lookfrom_pp(2) lookat_pp(2)], [lookfrom_pp(3) lookat_pp(3)], 'k')
grid
xlabel('x') 
ylabel('y') 
zlabel('z') 

%% 'desohomogeniza'

p1_pi = p1_pp/p1_pp(4);
%p1_pi = p1_pi(1:2)

p2_pi = p2_pp/p2_pp(4);
%p2_pi = p2_pi(1:2)

p3_pi = p3_pp/p3_pp(4);
%p3_pi = p3_pi(1:2)

figure
hold on;

plot3(px_pi, py_pi, pz_pi)
plot3([p1_pi(1) p2_pi(1) p3_pi(1) p1_pi(1)], [p1_pi(2) p2_pi(2) p3_pi(2) p1_pi(2)], [p1_pi(3) p2_pi(3) p3_pi(3) p1_pi(3)], '-o','Color','r','MarkerSize',10)

plot3(lookfrom_pp(1), lookfrom_pp(2), lookfrom_pp(3), '-o','Color','b','MarkerSize',14)
plot3([lookfrom_pp(1) lookat_pp(1)], [lookfrom_pp(2) lookat_pp(2)], [lookfrom_pp(3) lookat_pp(3)], 'k')
grid
xlabel('x') 
ylabel('y') 
zlabel('z') 

figure
hold on
plot(px_pi, py_pi)
plot([p1_pi(1) p2_pi(1) p3_pi(1) p1_pi(1)], [p1_pi(2) p2_pi(2) p3_pi(2) p1_pi(2)], '-o','Color','r','MarkerSize',6)
title('Plano imagem')
axis([-1 1 -1 1])
axis equal
grid
xlabel('x')
ylabel('y')
zlabel('z')

%% viewport

figure
subplot(1,2,1);
hold on
plot(px_pi, py_pi)
plot([p1_pi(1) p2_pi(1) p3_pi(1) p1_pi(1)], [p1_pi(2) p2_pi(2) p3_pi(2) p1_pi(2)], '-o','Color','r','MarkerSize',6)
title('Plano imagem')
axis([-1 1 -1 1])
grid
xlabel('x')
ylabel('y')
zlabel('z')

subplot(1,2,2);
px_j = [0 200 200 0 0]
py_j = [0 0 200 200 0]

plot(px_j, py_j)
title('Janela')
axis([-300 300 -300 300])
grid

umax = 200;
umin = 0;
vmax = 200;
vmin = 0;
xmax = 0.1;
xmin = -0.1;
ymax = 0.1;
ymin = -0.1;

sx = (umax - umin)/(xmax - xmin)
sy = (vmax - vmin)/(ymax - ymin)

T_tran1 = [1 0 0 -xmin;
           0 1 0 -ymin;
           0 0 1   0;
           0 0 0   1]

T_esc = [sx 0   0   0;
         0  sy  0   0;
         0  0   1   0;
         0  0   0   1]
     
T_tran2 = [1 0 0 umin;
           0 1 0 vmin;
           0 0 1  0;
           0 0 0  1]
     
T_vp = T_tran2*T_esc*T_tran1
 
p1_j = T_vp*p1_pi;
p2_j = T_vp*p2_pi;
p3_j = T_vp*p3_pi;

p1_j = p1_j(1:2)
p2_j = p2_j(1:2)
p3_j = p3_j(1:2)

keyboard

hold on
plot([p1_j(1) p2_j(1) p3_j(1) p1_j(1)], [p1_j(2) p2_j(2) p3_j(2) p1_j(2)], '-o','Color','r','MarkerSize',10)

%% questão 6 - interseção reta-esfera

% parametros da reta
u = [1 1 1]
o = [0 0 0]

% parametros da esfera
c = [4 2 2]
r = 2

% normaliza u
u = u/norm(u)

% encontra delta
delta = dot(u,(o-c))^2 - (norm(o-c)^2 - r^2)

% encontra as duas raizes
d1 = -dot(u, (o-c)) + sqrt(delta)
d2 = -dot(u, (o-c)) - sqrt(delta)

p_int = d2*u

[x,y,z] = sphere;
x = x*r;
y = y*r;
z = z*r;

keyboard

figure
surf(x+c(1), y+c(2), z+c(3))
hold on
plot3([0 6],[0 6],[0 6], 'r-')
plot3(p_int(1),p_int(2),p_int(3), 'ko', 'LineWidth',5)
axis equal