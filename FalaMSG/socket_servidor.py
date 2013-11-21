import socket, time, subprocess

HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

try:
    while True:
        con, cliente = tcp.accept()
        print 'Concetado por', cliente
        while True:            
            msg = con.recv(1024)
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
            
            print cliente, msg
            
        print 'Finalizando conexao do cliente', cliente
        con.close()

except KeyboardInterrupt:
    tcp.close()
