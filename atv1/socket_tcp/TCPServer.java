import java.io.*;
import java.net.*;

class TCPServer {
    
    public static void main(String args[]) throws Exception {
        String clientSentence;
        String capitalizedSentence;


        // Cria socket de aceitação na porta 6789
        ServerSocket welcomeSocket = new ServerSocket(6789);

        while (true) {

            // Espera, no socket de aceitação, por contato do cliente
            Socket connectionSocket = welcomeSocket.accept();

            // Cria stream de entrada ligado ao socket (in from client)
            BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));

            // Cria stream de saída ligado ao socket (out to client)
            DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());

            // Lê linha do socket
            clientSentence = inFromClient.readLine();

            if (clientSentence.equals("exit")) {
                outToClient.writeBytes("exiting...");
                break;
            }

            capitalizedSentence = clientSentence.toUpperCase() + '\n';

            // Escreve linha para o socket
            outToClient.writeBytes(capitalizedSentence);
        }
        welcomeSocket.close();
    }
}
