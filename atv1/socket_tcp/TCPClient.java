import java.io.*;
import java.net.*;

class TCPClient {

    public static void main(String args[]) throws Exception {
        String sentence;
        String modifiedSentence;

        // Cria stream de entrada (in from user)
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));

        // Cria socket cliente e conecta ao servidor
        Socket clientSocket = new Socket("hostname", 6789);
        
        // Cria stream de saída ligado ao socket (out to server)
        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());

        // Cria stream de entrada ligado ao socket
        BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

        sentence = inFromUser.readLine();

        // Envia linha para o servidor
        outToServer.writeBytes(sentence + '\n');

        // Lê linha do servidor
        modifiedSentence = inFromServer.readLine();

        System.out.println("FROM SERVER:" + modifiedSentence);

        clientSocket.close();

    }
}