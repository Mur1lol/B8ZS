import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Connection
from Server import Server
from Client import Client
from getIP import IP

# Line Coding
from CifraDeCesar import CifraDeCesar
from B8ZS import B8ZS

# Plotting
import matplotlib.pyplot as plt

class SelectorWindow:

    def __init__(self, master=None):
        # Connection
        self.server = Server()
        self.client = Client()

        # build ui
        self.window = tk.Tk() if master is None else tk.Toplevel(master)
        self.window.configure(
            background="#e6fff6",
            padx=30,
            pady=30,
            width=200)

        self.ip_label = tk.Label(self.window, text='IP:', background="#e6fff6", font=("poppins", 10))
        self.ip_label.grid(row=0, column=0, sticky='w')
        self.ip_input = tk.Entry(self.window)
        self.ip_input.grid(row=0, column=1, sticky='w')
        self.ip_input.insert(0, IP.get_local_ip())  # Adiciona um texto inicial
        #self.ip_input.bind("<FocusIn>", lambda event: self.on_entry_click(event, IP.get_local_ip()))
        #self.ip_input.bind("<FocusOut>", lambda event: self.on_focus_out(event, IP.get_local_ip()))


        self.port_label = tk.Label(self.window, text='Porta:', background="#e6fff6", font=("poppins", 10))
        self.port_label.grid(row=1, column=0, sticky='w')
        self.port_input = tk.Entry(self.window)
        self.port_input.grid(row=1, column=1, sticky='w')
        self.port_input.insert(0, '3000')  # Adiciona um texto inicial


        self.host = tk.Button(self.window, text='host', command=lambda: self.create_host(), background="#96ffd9", width=10)
        self.host.grid(row=3, column=0, pady=5, sticky='w')

        self.client_button = tk.Button(self.window, text='client', command=lambda: self.create_sender(), background="#96ffd9", width=10)
        self.client_button.grid(row=3, column=1, pady=5, sticky='w')

        self.window.title("Config")
        # Main widget
        self.mainwindow = self.window

    def on_entry_click(self, event, text):
        if self.ip_input.get() == text or self.port_input.get() == text:
            event.widget.delete(0, "end")  # Deleta o texto inicial
            event.widget.insert(0, '')  # Insere texto vazio
            event.widget.config(fg='black')  # Muda a cor do texto para preto

    def on_focus_out(self, event, text):
        if not event.widget.get():
            event.widget.insert(0, text)  # Restaura o texto inicial
            event.widget.config(fg='grey')  # Muda a cor do texto para cinza

    def run(self):
        self.mainwindow.mainloop()
    
    ## Creates a Sender Interface
    def create_sender(self):
        ip = self.ip_input.get()
        port = self.port_input.get()
    
        if port and ip:
            self.client.start(ip, int(port))
            self.window.destroy()
            self.host = MessageWindow('sender', self.server, self.client)
            self.host.run()
    
    ## Creates a Host Interface
    def create_host(self):
        ip = self.ip_input.get()
        port = self.port_input.get()
    
        if port and ip:
            self.server.start(ip, int(port))
            self.window.destroy()
            self.host = MessageWindow('host', self.server, self.client)
            self.host.run()

class MessageWindow:

    def receive_message(self):
        plt.close()
        # connection
        signal = self.server.receive_message()

        # line coding
        signal = self.b8.string_to_signal(signal)
        self.sig = signal
        binary = self.b8.decode(signal)

        # crypto
        self.binary_to_string = ''.join([str(item) for item in binary])
        
        self.cesar = self.crypt.binario_para_texto(self.binary_to_string)
        self.message = self.crypt.decifrar(self.cesar)
        
        #interface
        self.updateText()

        # graphic
        plt.step(list(range(len(signal))), signal)
        plt.show()

    def send_message(self):
        plt.close()
        self.message = self.message_input.get()
        self.cesar = self.crypt.cifrar(self.message)
        binary_message = self.crypt.texto_para_binario(self.cesar)
        self.binary_to_string = ''.join([str(item) for item in binary_message])
        self.sig = self.b8.encode(binary_message)

        #interface
        self.updateText()

        # graphic
        plt.step(list(range(len(self.sig))), self.sig)
        plt.show()

        # connection
        self.client.send_message(self.b8.signal_to_string(self.sig))

    def updateText(self):
        if self.fun == 'host':
             text = f"Signal: { self.sig }\nBinary: { self.binary_to_string } \nEncrypted Message: { self.cesar }\nMessage: { self.message } "
        else:
            text = f"Message: { self.message } \nEncrypted Message: { self.cesar }\nBinary: { self.binary_to_string } \nSignal: { self.sig }"
        self.message_data.delete("1.0","end")
        self.message_data.insert(tk.END, text)


    def __init__(self, fun, server, client, ip=0, port=0, master=None, ):
        # get connection values
        self.ip = ip
        self.port = port

        self.server = server
        self.client = client

        self.info = ''
        self.fun = fun

        self.crypt = CifraDeCesar(3)
        self.b8 = B8ZS()
        
        # build ui
        self.messageWindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.messageWindow.configure(
            background="#b6f2f0", height=200, width=200)
        self.title = tk.Label(self.messageWindow)
        self.title.configure(background="#b6f2f0", text='Message Data')
        self.title.pack(side="top")
        self.message_data = tk.Text(self.messageWindow)
        self.message_data.configure(height=20, width=100)
        self.message_data.pack(side="top")
        

        if fun != 'host':
            self.m_title = tk.Label(self.messageWindow)
            self.m_title.configure(background="#b6f2f0", text='Message')
            self.m_title.pack(side="top")
            self.message_input = tk.Entry(self.messageWindow)
            self.message_input.configure(width=50)
            self.message_input.pack(side="top")

        self.button = tk.Button(self.messageWindow)
        if fun == 'host':      
            self.button.configure(background="#e1effc", text='Receive', command=lambda: self.receive_message())
        else:
            self.button.configure(background="#e1effc", text='Send', command=lambda: self.send_message())
        
        self.button.pack(side="top")

        self.messageWindow.title(fun)

        # Main widget
        self.mainwindow = self.messageWindow

    def run(self):

        self.mainwindow.mainloop()
        