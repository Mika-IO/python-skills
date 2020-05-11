def validar_ip(ip):
    while True:
        # VERIFICAR SE A STRING TEM 3 PONTOS
        if ip.count('.') != 3:
            validar = 'Inválido'
            break
        # VERIFICAR SE TEM 4 CAMPOS
        campos = ip.split('.')
        if len(campos) != 4:
            validar = 'Inválido'
            break
        # VERIFICAR SE TODOS SÃO INTEIROS DE 0 Á 255
        for campo in campos:
            if campo not in range(256):
                validar = 'Inválido'
        validar = 'Válido' if validar not is 'Inválido'
        return validar
               