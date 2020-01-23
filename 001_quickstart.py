from glumpy import app, gloo, gl

vertex = """
	attribute vec2 position;
	void main() { gl_Position = vec4(position, 0.0, 1.0); } """

fragment = """
	void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); } """

# create window with a valid gl context
window = app.Window()

# build the program and corresponding buffers (with 4 vertices)
quad = gloo.Program(vertex, fragment, count=4)

# upload data into gpu
quad['position'] = (-1, +1), (+1, +1), (-1, -1), (+1, -1)

# tell glumpy what needs to be done at each redraw
@window.event
def on_draw(dt):
	window.clear()
	quad.draw(gl.GL_TRIANGLE_STRIP)

# run the app
app.run()
