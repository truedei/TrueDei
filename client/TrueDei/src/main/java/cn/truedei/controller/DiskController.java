package cn.truedei.controller;

import cn.truedei.entity.OsEntity;
import cn.truedei.socket.MyWebSocket;
import org.springframework.amqp.core.ExchangeTypes;
import org.springframework.amqp.rabbit.annotation.*;
import org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer;
import org.springframework.amqp.rabbit.listener.MessageListenerContainer;
import org.springframework.amqp.rabbit.listener.RabbitListenerEndpointRegistry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.thymeleaf.util.ArrayUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;
import java.util.concurrent.CopyOnWriteArraySet;

@Controller
@RequestMapping("cn/truedei/")
@Component
public class DiskController {

    @RequestMapping("disk")
    public String disk(){
        return "admin/disk";
    }

    RabbitListenerEndpointRegistry rabbitListenerEndpointRegistry = null;
    static {
        RabbitListenerEndpointRegistry rabbitListenerEndpointRegistry = new RabbitListenerEndpointRegistry();
    }

    //关闭和开启DiskData
    @RequestMapping("startAndStopDiskData")
    @ResponseBody
    public String startAndStopDiskData(){
//           Set<String> ids = rabbitListenerEndpointRegistry.getListenerContainerIds();
//        for (String id : ids) {
//            System.out.println("id="+id);
//        }
        boolean stop = stop("truedei.linux.topic.disk.data.queue");
//        MessageListenerContainer diskData = rabbitListenerEndpointRegistry.getListenerContainer("diskData");
////        rabbitListenerEndpointRegistry.stop();
//        diskData.stop();
        //1、获取监听的容器
//        MessageListenerContainer diskData = rabbitListenerEndpointRegistry.getListenerContainer("diskData");
//        System.out.println("现在的状态："+diskData.isRunning());
//        //2、开启/关闭容器
//        if(!diskData.isRunning()){
//            diskData.start();
//            System.out.println("开启DiskData");
//        }else{
//            diskData.stop();
//            System.out.println("关闭DiskData");
//        }

        return String.valueOf(stop);
    }

    /**
     * 判断监听器是否监听了指定的队列。
     * @param queueName 队列名称
     * @param listenerContainer 监听容器
     * @return true-监听，false-未监听。
     */
    private boolean isQueueListener(String queueName, MessageListenerContainer listenerContainer) {
        if (listenerContainer instanceof AbstractMessageListenerContainer) {
            AbstractMessageListenerContainer abstractMessageListenerContainer = (AbstractMessageListenerContainer) listenerContainer;
            String[] queueNames = abstractMessageListenerContainer.getQueueNames();
            return ArrayUtils.contains(queueNames, queueName);
        }
        return false;
    }

    public boolean stop(String queueName) {
        Collection<MessageListenerContainer> listenerContainers = this.rabbitListenerEndpointRegistry.getListenerContainers();
        for (MessageListenerContainer listenerContainer : listenerContainers) {
            if (this.isQueueListener(queueName, listenerContainer)) {
                listenerContainer.stop();
                return true;
            }
        }
        return false;
    }

    public void start() {
        this.rabbitListenerEndpointRegistry.start();
    }



//    @Autowired
//    private RabbitListenerEndpointRegistry rabbitListenerEndpointRegistry;
//
//    public void stopAll() {
//        this.rabbitListenerEndpointRegistry.stop();
//    }

//    @Autowired
//    private RabbitListenerEndpointRegistry   rabbitListenerEndpointRegistry;
//
//    public void rabbitMqListenerStartAndStopTest(){
//        //1.获取监听的容器
//        MessageListenerContainer container = rabbitListenerEndpointRegistry.getListenerContainer("diskData");
//        //2.开启容器
//        if(!container.isRunning()){
//            container.start();
//            System.out.println("开启容器");
//        }
//    }


    @RabbitListener(
            //关闭自动开启的功能
            autoStartup = "true",
            //定义一个ID，为了使用Java手动开启
            id = "diskData",
            //绑定监听的队列
            bindings = @QueueBinding(value = @Queue(value = "${truedei.rabbitmq.topic.disk.data.queue}",
            //是否持久化  autoDelete = "false":持久化，autoDelete = "true"：相反
            autoDelete = "false"),
            //指定交换机的名字
            exchange = @Exchange(value = "${truedei.rabbitmq.topic.exchangeName}",type = ExchangeTypes.TOPIC),
            //指定路由key，通过这个路由key过滤消息，只允许以disk.data为前缀的进来
            key = "disk.data" //路由Key
    ))
    @RabbitHandler
    public void DiskData(String Message){
        System.out.println("收到Linux的监控消息--------->"+Message);
        String str = Message;
        if(str!=null){
//          System.out.println(str);
            str = str.substring(1,str.length()-1);
//          System.out.println(str);
            String[] split = str.split("', '");
            List<OsEntity> osEntities = new ArrayList<>();

            for (String s : split) {
                s = s.substring(1,s.length());
//                System.out.println(s);
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

//            System.out.println(msg);
            System.out.println("收到消息");
            sendMsg(msg);
        }
        try {
            Thread.sleep(200);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @RabbitListener(
            //关闭自动开启的功能
            autoStartup = "false",
            id = "diskWarning",
            //绑定监听的队列
            bindings = @QueueBinding(value = @Queue(value = "${truedei.rabbitmq.topic.disk.warning.queue}",
                    //是否持久化  autoDelete = "false":持久化，autoDelete = "true"：相反
                    autoDelete = "false"),
                    //指定交换机的名字
                    exchange = @Exchange(value = "${truedei.rabbitmq.topic.exchangeName}",type = ExchangeTypes.TOPIC),
                    //指定路由key，通过这个路由key过滤消息，只允许报警信息进来
                    key = "disk.warning" //路由Key
            ))
    @RabbitHandler
    public void DiskWarnings(String Message){
        System.out.println("收到Linux的报警消息--------->"+Message);
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
