import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
	glut.glutSwapBuffers()

def reshape(width, height):
	gl.glViewport(0, 0, width, height)

def keyboard(key, x, y):
	if key == b'\x1b':
		sys.exit(0)

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
glut.glutCreateWindow("glut window")
glut.glutReshapeWindow(512, 512)
glut.glutReshapeFunc(reshape)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()


# need to request program and shader slots from the GPU
program = gl.glCreateProgram()
vertex = gl.glCreateShader(gl.GL_VERTEX_SHADER)
fragment = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)


# ask for the compilation of our shaders into GPU objects and we log for any error
vertex_code = """
	attribute vec2 position;
	void main() { gl_Position = vec4(position, 0.0, 1.0); } """

fragment_code = """
	void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); } """

# Set shaders source
gl.glShaderSource(vertex, vertex_code)
gl.glShaderSource(fragment, fragment_code)

# Compile shaders
gl.glCompileShader(vertex)
if not gl.glGetShaderiv(vertex, gl.GL_COMPILE_STATUS):
    error = gl.glGetShaderInfoLog(vertex).decode()
    print(error)
    raise RuntimeError("Vertex shader compilation error")

gl.glCompileShader(fragment)
if not gl.glGetShaderiv(fragment, gl.GL_COMPILE_STATUS):
    error = gl.glGetShaderInfoLog(fragment).decode()
    print(error)
    raise RuntimeError("Fragment shader compilation error")

# link our two objects in into a program and again
# we check for errors during the process
gl.glAttachShader(program, vertex)
gl.glAttachShader(program, fragment)
gl.glLinkProgram(program)

if not gl.glGetProgramiv(program, gl.GL_LINK_STATUS):
    print(gl.glGetProgramInfoLog(program))
    raise RuntimeError('Linking error')
