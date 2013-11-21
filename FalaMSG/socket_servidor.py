import socket, lcdlib, time, subprocess

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
lcd = lcdlib.lcd(0x20, 1)
lcd.print_s("Iniciando app", 1)
time.sleep(2)

try:
    while True:
        lcd.clear()
        lcd.print_s("Aguardando msg", 1)
        con, cliente = tcp.accept()
        print 'Concetado por', cliente
        lcd.clear()
        lcd.print_s("Cliente OK", 1)
        lcd.print_s(cliente[0], 2)
        time.sleep(2)
        while True:            
            msg = con.recv(1024)
            lcd.clear()
            if not msg: break
            msg_resp = str(len(msg)) + " caracteres recebidos"
            con.send(msg_resp)
            
            url = "http://translate.google.com/translate_tts?ie=UTF-8&tl=pt&q=" + msg
            print url
            cmd = "mplayer -user-agent -really-quiet Mozilla \"" + url + "\""
            process = subprocess.Popen(cmd, shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)
            out, err = process.communicate()
            errcode = process.returncode
            #print out,err,errcode
            
            lcd.print_s(msg,1)
            time.sleep(1)
            if len(msg) > 16:
                for i in range(len(msg)-15):
                    lcd.scroll_display_left()
                    time.sleep(1)
            print cliente, msg
            
        print 'Finalizando conexao do cliente', cliente
        lcd.clear()
        lcd.print_s("Cliente OFF", 1)
        lcd.print_s(cliente[0], 2)
        time.sleep(2)
        lcd.clear()
        lcd.print_s("Nenhum cliente", 1)
        lcd.print_s("conectado agora", 2)
        con.close()

except KeyboardInterrupt:
    lcd.clear()
    lcd.print_s("Encerrando 2s", 1)
    for i in range(2):
        lcd.print_s(str(2-i), 2)
        time.sleep(1)
    lcd.clear()
    tcp.close()
