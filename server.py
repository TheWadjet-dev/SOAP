from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HolaMundoService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Unicode)
    def decir_hola(ctx, nombre, veces):
        return f"Hola, {nombre}! " * veces

app = Application([HolaMundoService],
                  tns='spyne.holamundo',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 3000, WsgiApplication(app))
    print("Servidor SOAP en http://localhost:3000")
    server.serve_forever()
