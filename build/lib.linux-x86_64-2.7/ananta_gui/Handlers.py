from tornado.web import RequestHandler
import app as ap
file_load_st1="import ananta_base.data_io as dio \n\
from ananta_base.data_set import TrainingSet\n\
t=TrainingSet()\n\
fp = dio.FileLoadingProfile()\n\
fs = dio.FileLoadStep(\"csv\",\"/home/lakmal/PycharmProjects/GSOM/data.csv\")\n\
fp.addStep(fs)\n\
T= fp.execute(t)\n\
outp = T.data.describe().__repr__()\n\
fi = open(\"/home/lakmal/PycharmProjects/AnantaFramework/ananta_gui/cache/des.txt\",\"w\")\n\
fi.write(str(outp))\n\
strcols = []\n\
for column in T.data.columns:\n\
\tstrcols.append(column)\n\
fi.close()\n\
fi= open(\"/home/lakmal/PycharmProjects/AnantaFramework/ananta_gui/cache/fies.txt\",\"w\")\n\
fi.write(str(strcols))\n\
fi.close()"




class DesReadHandler(RequestHandler):

    def get(self):
        f = open('./cache/fies.txt','r')
        strn = f.read()
        print strn
        f.close()
        self.write(str(strn))

class HelloHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")
'''
'''

class TestHandler(RequestHandler):

    def get(self):
        ap._chan.execute("f=open(\"/home/gilgamesh/hello.txt\",\"a\")")
        ap._chan.execute("f.write(str('wimal weerawansa ')+str(i)+str(' paarak charter'))\n")
        _handle_msg(ap._chan.get_msg())
        ap._chan.execute("i+=1")
        self.write("check the file")

def _handle_msg(st):

    if st['content']['status']=="ok":
        print "everything worked"
    else:
        print st['content']['traceback']


class FileLoadHandler(RequestHandler):
    def get(self):
        c=ap._chan
        print "now at request handler"
        file_ar= self.get_arguments('file')[0]
        #ap._chan.execute(file_load_st1+file_ar+file_load_st1, allow_stdin=True)
        #c.execute("fi=open(\"/home/gilgamesh/hello.txt\",\"a\")")
        #c.execute("fi.write('"+file_ar+"')")
        #c.execute("fi.close()")
        c.execute(file_load_st1)
        st= ap._chan.get_msg()
        print "code executed"
        if st['content']['status']=="ok":
            self.write("OK")
        else:
            self.write(str(st['content']['traceback']))