
//返回访问者IP
document.write("<script src='http://pv.sohu.com/cityjson?ie=utf-8'></script>");
// document.write('IP地址:' + returnCitySN["cip"] + ', CID:' + returnCitySN["cid"] + ', 地区:' + returnCitySN["cname"]+",浏览器版本:"+getBrowserInfo());

//封装这些数据
function getInfoData() {
    var map = new Map();
    map.set("cip",returnCitySN["cip"]);
    map.set("cid",returnCitySN["cid"]);
    map.set("cname",returnCitySN["cname"]);
    map.set("cip",returnCitySN["cip"]);
    map.set("browserInfo", getBrowserInfo());
    return map;
}

//返回浏览器版本
function getBrowserInfo()
{
    var agent = navigator.userAgent.toLowerCase() ;

    var regStr_ie = /msie [\d.]+;/gi ;
    var regStr_ff = /firefox\/[\d.]+/gi
    var regStr_chrome = /chrome\/[\d.]+/gi ;
    var regStr_saf = /safari\/[\d.]+/gi ;

    //IE
    if(agent.indexOf("msie") > 0)
    {
        return agent.match(regStr_ie) ;
    }

    //firefox
    if(agent.indexOf("firefox") > 0)
    {
        return agent.match(regStr_ff) ;
    }

    //Chrome
    if(agent.indexOf("chrome") > 0)
    {
        return agent.match(regStr_chrome) ;
    }

    //Safari
    if(agent.indexOf("safari") > 0 && agent.indexOf("chrome") < 0)
    {
        return agent.match(regStr_saf) ;
    }

}

//获取时间
function current(){
    var d=new Date(),str='';
    str +=d.getFullYear()+'年'; //获取当前年份
    str +=d.getMonth()+1+'月'; //获取当前月份（0——11）
    str +=d.getDate()+'日';
    str +=d.getHours()+'时';
    str +=d.getMinutes()+'分';
    str +=d.getSeconds()+'秒';
    return str;
}
