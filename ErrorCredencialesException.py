class ErrorCredencialesException(Exception):
    pass
    #esta es una exception particular para manejar e errrStatus 401
    #que corresponde al acceso denegado que se genera al ingresar
    #incorectamente alguno de los parametros de la credencial brindada por twitter