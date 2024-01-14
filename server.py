'''import socket
import wx

# Создаем серверный сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 7777))
server_socket.listen(1)

# Создаем GUI
app = wx.App()
frame = wx.Frame(None, title='Server', size=(200, 200))
frame.SetBackgroundColour(wx.WHITE)
frame.Show()
app.MainLoop()

# Ждем получение числа от клиента и меняем фон GUI
while True:
    client_socket, address = server_socket.accept()
    number = client_socket.recv(1024).decode()
    if number == '1':
        frame.SetBackgroundColour(wx.GREEN)
        frame.Refresh()
        frame.Update()

# Запускаем main loop GUI

'''





''' v2
import socket
import wx
import threading

class ServerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Server', size=(200, 200))
        self.SetBackgroundColour(wx.WHITE)

    def on_wait_for_number(self, event):
        # Ожидаем получение числа от клиента и меняем фон GUI
        client_socket, address = self.server_socket.accept()
        number = client_socket.recv(1024).decode()
        if number == '1':
            self.SetBackgroundColour(wx.GREEN)
            self.Refresh()
        client_socket.close()

def run_gui():
    app = wx.App()
    frame = ServerFrame()
    frame.Show()

    # Создаем серверный сокет внутри GUI потока
    frame.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    frame.server_socket.bind(('localhost', 7777))
    frame.server_socket.listen(1)

    # Привязываем функцию к кнопке внутри GUI потока
    button = wx.Button(frame, label='Wait for number', pos=(10, 10))
    button.Bind(wx.EVT_BUTTON, frame.on_wait_for_number)

    app.MainLoop()

if __name__ == '__main__':
    # Запускаем GUI в отдельном потоке
    gui_thread = threading.Thread(target=run_gui)
    gui_thread.start()

    # Ждем получение числа от клиента и меняем фон GUI
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 7777))
    server_socket.listen(1)
    while True:
        client_socket, address = server_socket.accept()
        number = client_socket.recv(1024).decode()
        if number == '1':
            wx.CallAfter(wx.GetApp().GetTopWindow().SetBackgroundColour, wx.GREEN)
            wx.CallAfter(wx.GetApp().GetTopWindow().Refresh)
        client_socket.close()
'''



import socket
import wx
import threading

class ServerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Server', size=(200, 200))
        self.SetBackgroundColour(wx.WHITE)

    def on_wait_for_number(self, event):
        # Ожидаем получение числа от клиента и меняем фон GUI
        client_socket, address = self.server_socket.accept()
        number = client_socket.recv(1024).decode()
        if number == '1':
            self.SetBackgroundColour(wx.RED)
            self.Refresh()
        if number == '0':
            self.SetBackgroundColour(wx.WHITE)
            self.Refresh()

def run_gui():
    app = wx.App()
    frame = ServerFrame()
    frame.Show()

    app.MainLoop()

if __name__ == '__main__':
    # Создаем серверный сокет в главном потоке
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 7777))
    server_socket.listen(1)

    # Запускаем GUI в отдельном потоке, передавая ему сокет
    gui_thread = threading.Thread(target=run_gui, args=())
    gui_thread.start()

    # Ждем получение числа от клиента и меняем фон GUI
    client_socket, address = server_socket.accept()
    while True:
        number = client_socket.recv(1024).decode()
        if number == '1':
            wx.CallAfter(wx.GetApp().GetTopWindow().SetBackgroundColour, wx.GREEN)
            wx.CallAfter(wx.GetApp().GetTopWindow().Refresh)
        else:
            wx.CallAfter(wx.GetApp().GetTopWindow().SetBackgroundColour, wx.WHITE)
            wx.CallAfter(wx.GetApp().GetTopWindow().Refresh)