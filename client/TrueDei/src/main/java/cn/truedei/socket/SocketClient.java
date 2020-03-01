package cn.truedei.socket;

import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;

public class SocketClient {

    static  public void socket(){
        try {
            Socket socket = new Socket("47.105.166.27", 17549);
            if (socket.isConnected()) {
                // 如果连接成功了就开启写和读的进程
//            new writer(socket).start();
                new reada(socket).start();

            } else {
                System.out.println("服务器未开启");
            }

        } catch (UnknownHostException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
