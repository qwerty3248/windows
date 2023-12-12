import turtle

def dibujar_corazon():

	# Configurar la tortuga
	t = turtle.Turtle()
	t.speed(2)
	t.pensize(3)
	t.color("red")

	# Dibujar el corazón
	t.begin_fill()
	t.fillcolor("red")
	t.left(50)
	t.forward(133)
	t.circle(50, 200)
	t.right(140)
	t.circle(50, 200)
	t.forward(133)
	t.end_fill()

# Dibujar el corazón
dibujar_corazon()

# Mover la tortuga a la posición para escribir el mensaje
turtle.penup()
turtle.goto(0, -180)
turtle.pendown()

# Escribir el mensaje
turtle.color("black")
turtle.write("GUAPA ROSSANA!!!", align="center", font=("Arial", 25, "normal"))

# Mantener la ventana abierta
turtle.mainloop()

