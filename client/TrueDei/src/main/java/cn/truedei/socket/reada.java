package cn.truedei.socket;

import cn.truedei.entity.OsEntity;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.CopyOnWriteArraySet;

// 从通道中读取的线程
public class reada extends Thread {
    private Socket socket;
    private BufferedReader bufferedReader;
    private String str = null;

    public reada(Socket socket) throws IOException {
        this.socket = socket;
        this.bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

    @Override
    public void run() {
        try {
            while (true) {
                    str = bufferedReader.readLine();
                    if(str!=null){
//                        System.out.println(str);
                        str = str.substring(1,str.length()-1);
//                        System.out.println(str);
                        String[] split = str.split("', '");
                        List<OsEntity> osEntities = new ArrayList<>();

                        for (String s : split) {
                            s = s.substring(1,s.length());
                            System.out.println(s);
                            String[] split1 = s.split(",");
                            osEntities.add(new OsEntity(split1[0],split1[1],split1[2],split1[3],split1[4],split1[5]));
                        }

                        String msg = "";

                        for (OsEntity osEntity : osEntities) {
                            msg = msg + osEntity.toString()+",";
//                            System.out.println(osEntity.toString());
                        }

                        //组装成JSON数据格式
                        msg = "["+msg.substring(0,msg.length()-1)+"]";

                        System.out.println(msg);
                        sendMsg(msg);
                    }
                try {
                    Thread.sleep(200);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
        }
    }

    //推送消息
   static public void sendMsg(String msg){
        System.err.println("*********  任务执行   **************");
        CopyOnWriteArraySet<MyWebSocket> webSocketSet =MyWebSocket.getWebSocketSet();
        webSocketSet.forEach(c->{
            try {
//                c.sendMessage(" 发送  " +msg +"---"+ new Date().toLocaleString());
                //发送
                c.sendMessage(msg);
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        System.err.println(".......任务完成.......");
    }
}