package cn.truedei.entity;

public class OsEntity {
    private String Filesystem;
    private String Size;
    private String Used;
    private String Avail;
    private String Useb; //使用百分比
    private String Mounted;

    public OsEntity() {
    }

    public OsEntity(String filesystem, String size, String used, String avail, String useb, String mounted) {
        Filesystem = filesystem;
        Size = size;
        Used = used;
        Avail = avail;
        Useb = useb;
        Mounted = mounted;
    }

    //封装成JSON数据格式
    @Override
    public String toString() {
        return "{" +
                "\"Filesystem\":\"" + Filesystem + '\"' +
                ", \"Size\":\"" + Size + '\"' +
                ", \"Used\":\"" + Used + '\"' +
                ", \"Avail\":\"" + Avail + '\"' +
                ", \"Useb\":\"" + Useb + '\"' +
                ", \"Mounted\":\"" + Mounted + '\"' +
                '}';
    }

    public String getFilesystem() {
        return Filesystem;
    }

    public void setFilesystem(String filesystem) {
        Filesystem = filesystem;
    }

    public String getSize() {
        return Size;
    }

    public void setSize(String size) {
        Size = size;
    }

    public String getUsed() {
        return Used;
    }

    public void setUsed(String used) {
        Used = used;
    }

    public String getAvail() {
        return Avail;
    }

    public void setAvail(String avail) {
        Avail = avail;
    }

    public String getUseb() {
        return Useb;
    }

    public void setUse(String useb) {
        Useb = useb;
    }

    public String getMounted() {
        return Mounted;
    }

    public void setMounted(String mounted) {
        Mounted = mounted;
    }
}
