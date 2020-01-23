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
