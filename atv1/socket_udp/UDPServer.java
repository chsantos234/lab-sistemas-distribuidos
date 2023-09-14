package socket_udp;
import java.io.*;
import java.net.*;

class UDPServer {
    public static void main(String args[]) throws Exception {
        
        // Cria socket datagrama na porta 9876
        DatagramSocket serverSocket = new DatagramSocket(9876);

        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];

        while (true) {

            // Cria espaço para datagramas recebidos
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

            // Recebe datagrama
            serverSocket.receive(receivePacket);

            String sentence = new String(receivePacket.getData());

            // Obtém endereço IP do transmissor
            InetAddress IPAddress = receivePacket.getAddress();

            // Obtém número da porta do transmissor
            int port = receivePacket.getPort();

            if (sentence.equals("exit")) {
                String exit = "exiting...";
                sendData = exit.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);
                serverSocket.send(sendPacket);
                break;
            }

            String capitalizedSentence = sentence.toUpperCase();

            sendData = capitalizedSentence.getBytes();

            // Cria datagrama para enviar ao cliente
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);

            // Escreve o datagrama para dentro do socket
            serverSocket.send(sendPacket);
        }
        serverSocket.close();
    }
}
