import threading
import time
import subprocess


class ThreadingExample(object):
    foto = None
    fecha_hora = None
    user_logeado = None

#foto,hora, user
    def __init__(self, foto, fecha_hora, user_logeado):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.foto = foto
        self.fecha_hora = fecha_hora
        self.user_logeado = user_logeado

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = False                            # No Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        #while True:
        #    time.sleep(10)
        # ./demos/classifier.py infer ./generated-embeddings/classifier.pkl fotosTest/fotosWeb/alexander.jpg
        commando2 = ["./demos/classifier.py", "infer", "--multi", "./generated-embeddings/classifier.pkl", self.foto]
        proc2 = subprocess.Popen(commando2, cwd="/home/pamela/Escritorio/openface", stdout=subprocess.PIPE)
        out2 = proc2.communicate()
        print out2[0]
        # guaardaer en la base lod resultados


# id_user_log = 1
# ahoritas="ahoritas"
# example = ThreadingExample(foto="/home/pamela/Escritorio/openface/fotosTest/fotosWeb/alexander.jpg", user_logeado=id_user_log, fecha_hora=ahoritas)
