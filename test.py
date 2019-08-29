#动态服务器组
upstream dynamic_zuoyu {
    ip_hash;    #实现每个url定向到同一个后端服务器
    server localhost:8080;  #tomcat 7.0
    server localhost:8081;  #tomcat 8.0
    server localhost:8082;  #tomcat 8.5
    server localhost:8083;  #tomcat 9.0
}
