from Facade.chaeyeon import ChaeyeonServer
from Facade.jungyin import JungyinServer

class Bankq:
    def __init__(self):
        self.chaeyeon = ChaeyeonServer()
        self.jungyin = JungyinServer()

    def 이사(self):
        print("bankq 이사를 시작합니다")
        self.chaeyeon.랜선정리()
        self.jungyin.청소()


if __name__ == '__main__':
    bankq = Bankq()
    bankq.이사()
