import win32com.client
import pythoncom
import sys

class XASessionReceiver:
    def __init__(self):
        self.parent = None

class XASession:
    def __init__(self, login_server):
        self.login_server = self.set_server(login_server=login_server)
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionReceiver)

    @staticmethod
    def set_server(login_server):
        if login_server == "실투자":
            return "hts.ebestsec.co.kr"
        elif login_server == "모의투자":
            return "demo.ebestsec.co.kr"

    def connect_server(self):
        res = self.session.ConnectServer(self.login_server, 20001)
        print(res)
        