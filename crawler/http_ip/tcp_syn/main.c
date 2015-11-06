#include "stdio.h"
//#include "tcp_syn.h"
#include "netinet/in.h"
#include "sys/socket.h"
#include "netdb.h"

int main()
{
    int sockfd = socket(AF_INET, SOCK_RAW, 1);

    struct sockaddr_in target;
    char *ip= "www.baidu.com";
    char *ip1 = "11.1.1.1";
    struct hostent* host = gethostbyname(ip1);
    target.sin_addr = *((struct in_addr *)host->h_addr);
    target.sin_family = AF_INET;
    target.sin_port=htons(0);



    //test();
    send_v4(sockfd, &target);
    recv_v4(sockfd, &target);
    test(); 
    proc_v4();
    return 0;
}
