def gordon(a):
    # your code here
    a=a.upper()
    mensaje = a.replace("A", "@")
    mensaje = mensaje.replace("E", "*")
    mensaje = mensaje.replace("I", "*")
    mensaje = mensaje.replace("O", "*")
    mensaje = mensaje.replace("U", "*")
    mensaje = mensaje.replace(" ", "!!!! ")
    mensaje = mensaje + '!!!!'
    
    return mensaje