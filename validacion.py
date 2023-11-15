def validacion(usuario1, contraseña1):
    usuario = "InnovaCode"
    contraseña = "CodingCorporation"
    validado = False
    if (usuario == usuario1) and (contraseña == contraseña1):
        print("Acceso permitido")
        validado = True
    else: 
        print("Acceso denegado, contraseña o usuarios incorrectos")
    return validado