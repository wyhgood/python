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
    struct hostent* host = gethostbyname(ip);
    target.sin_addr = *((struct in_addr *)host->h_addr);
    target.sin_family = AF_INET;
    target.sin_port=htons(0);



    test();
    send_v4(sockfd, &target);
    //proc_v4();
}
