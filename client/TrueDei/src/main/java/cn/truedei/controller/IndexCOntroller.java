package cn.truedei.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class IndexCOntroller {

    @RequestMapping("/")
    public String index(){
        return "trueder/index";
    }

    @RequestMapping("/admin")
    public String admin(){
        return "admin/index";
    }

    @RequestMapping("/soc")
    public String soc(){
        return "admin/sock";
    }
}
