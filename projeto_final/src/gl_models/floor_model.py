from OpenGL import GL as gl


def draw_floor(texture_id: int):
    """
        Modelo do chão.
        Basicamente desenha um quadrado 20x20 com uma textura

        (10,-10)--------------------------(-10,-10)             
            |                             |     
            |                             | 
            |                             |
        (10.10) ------------------------(-10,10) #(x,z)
    """
    gl.glColor4f(1.0, 1.0, 1.0, 1.0)

    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
    gl.glBegin(gl.GL_QUADS)

    gl.glTexCoord2fv([0.0, 0.0])
    gl.glVertex3f(10, 0, 10)

    gl.glTexCoord2fv([1.0, 0.0])  # (x,y)
    gl.glVertex3f(-10, 0, 10)

    gl.glTexCoord2fv([1.0, 1.0])
    gl.glVertex3f(-10, 0, -10)

    gl.glTexCoord2fv([0.0, 1.0])
    gl.glVertex3f(10, 0, -10)

    gl.glEnd()
    
