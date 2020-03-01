package cn;

import cn.truedei.socket.SocketClient;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class TruedeiApplication {

    public static void main(String[] args) {
        SpringApplication.run(TruedeiApplication.class, args);
        //开启socket与linux的socket通信
//        SocketClient.socket();
    }

}
