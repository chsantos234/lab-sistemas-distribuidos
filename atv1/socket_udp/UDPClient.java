package socket_udp;
import java.io.*;
import java.net.*;

class UDPClient {
    public static void main(String args[]) throws Exception {
    
        // Cria stream de entrada (in from user)
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        
        // Cria socket de cliente
        DatagramSocket clientSocket = new DatagramSocket();

        // Translada nome do hospedeiro para endereço IP usando DNS
        InetAddress IPAddress = InetAddress.getByName("hostname");

        byte[] sendData = new byte[1024];
        byte[] receiveData = new byte[1024];

        String sentence = inFromUser.readLine();
        sendData = sentence.getBytes();

        // Cria datagrama com dados a enviar, tamanho, endereço IP porta
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);

        // Envia datagrama para servidor
        clientSocket.send(sendPacket);

        // Cria espaço para datagramas recebidos
        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        
        // Recebe datagrama
        clientSocket.receive(receivePacket);

        // Lê datagrama do servidor
        String modifiedSentence = new String(receivePacket.getData());

        System.out.println("FROM SERVER:" + modifiedSentence);
        clientSocket.close();
    }
}
