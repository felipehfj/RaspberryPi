<html>
    <title>RPi - Sistema de Mensagem</title>
    <body>
        <formset>
            <form method="POST" action="lcd.php">
                <input type="text" name="texto" />
                <input type="submit" value="Enviar" name="enviar">
                <input type="reset" value="Limpar" name="limpar">
            </form>
        </formset>
    </body>
</html>

<?php

    $host    = "127.0.0.1";
    $porta   = 5000;

    if(isset($_POST['texto'])){

        $mensagem = $_POST['texto'];

        echo "Mensagem enviada ao servidor LCD: ".$mensagem;
        // criando o socket
        $socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Impossivel criar socket\n");
        // conectando com o servidor
        $resultado = socket_connect($socket, $host, $porta) or die("Impossivel conectar ao servidor\n");  
        // enviando mensagem ao servidor
        socket_send($socket, $mensagem, strlen($mensagem), 0) or die("Impossivel enviar dados ao servidor\n");
        // obtendo resposta do servidor
        $resultado = socket_read ($socket, 1024) or die("Impossivel ler a resposta do servidor\n");
        echo "<br /> Resposta do servidor: ".$resultado;
        // fechando conexão com o servidor
        socket_close($socket);  
    }
?>
