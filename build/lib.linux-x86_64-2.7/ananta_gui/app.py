__author__ = 'gilgamesh'

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url, StaticFileHandler
from IPython.kernel.manager import KernelManager
import Handlers

_man=KernelManager()
_man.start_kernel()

_cli = _man.client()
_cli.start_channels()
_chan = _cli.shell_channel
_chan.execute("i=0")

def make_app():
    return Application([
        (r"/static/(.*)", StaticFileHandler, {"path": "/home/lakmal/PycharmProjects/AnantaFramework/ananta_gui/html"}),
        url(r"/", Handlers.HelloHandler),
        url(r"/ws/load",Handlers.FileLoadHandler),
        url(r"/ws/read_des",Handlers.DesReadHandler),

        url(r"/ws/test/",Handlers.TestHandler)
        ])

def main():
    app = make_app()
    app.listen(8800)
    IOLoop.current().start()


if __name__ == "__main__":
    main()