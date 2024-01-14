import socket
import wx

class ClientFrame(wx.Frame):
    def __init__(self):
        self.number = 1
        super().__init__(None, title='Client', size=(200, 200))
        self.SetBackgroundColour(wx.WHITE)

        # Создаем текстовые поля и кнопки
        host_label = wx.StaticText(self, label='Host:', pos=(10, 10))
        self.host_text = wx.TextCtrl(self, pos=(50, 10))
        port_label = wx.StaticText(self, label='Port:', pos=(10, 40))
        self.port_text = wx.TextCtrl(self, pos=(50, 40))
        connect_button = wx.Button(self, label='Connect', pos=(10, 70))
        send_button = wx.Button(self, label='Send', pos=(100, 70))

        # Привязываем функции к кнопкам
        connect_button.Bind(wx.EVT_BUTTON, self.on_connect)
        send_button.Bind(wx.EVT_BUTTON, self.on_send)

        # Создаем клиентский сокет
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def on_connect(self, event):
        # Получаем данные из текстовых полей
        host = self.host_text.GetValue()
        port = int(self.port_text.GetValue())

        # Подключаемся к серверному сокету
        self.client_socket.connect((host, port))

    def on_send(self, event):
        # Отправляем серверному сокету цифру 1 или 0
        self.client_socket.send(str(self.number).encode())
        if(self.number==1):
            self.number = 0
        else:
            self.number = 1

if __name__ == '__main__':
    # Создаем GUI и запускаем main loop
    app = wx.App()
    frame = ClientFrame()
    frame.Show()
    app.MainLoop()