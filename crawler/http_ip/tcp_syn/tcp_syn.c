#include "tcp_syn.h"
#include "stdio.h"
#include "sys/socket.h"
#include "netdb.h"
#include "netinet/in.h"

#define BUFSIZE 1500

void
test()
{
    printf("abdc\n");
}

void
send_v4(int sockfd, struct sockaddr_in *tar)
{
    int len;
    struct icmp *icmp;
    char sendbuf[BUFSIZE];
    //sockfd = socket(AF_INET, SOCK_RAW, 1);
    printf("dddddddddddd\n");
    // = "111.11.111.1";
    //inet_aton("11.11.11.1", &addrptr);
    //char *ip= "www.baidu.com";
    //struct hostent* host = gethostbyname(ip);

    //target.sin_addr = *((struct in_addr *)host->h_addr);
    //printf("eeeeeeee\n");
    //target.sin_family = AF_INET;
    printf("aaaaaaaaaaaa\n");
    //target.sin_port=htons(0);
    printf("ccccccccccccccc\n");
    printf("aaaaaaaaaaaaa\n");

    icmp = (struct icmp *) sendbuf;
    icmp->icmp_type = ICMP_ECHO;
    icmp->icmp_code = 0;
    icmp->icmp_id = getpid();
    icmp->icmp_seq = nsent++;
    memset(icmp->icmp_data, 0xa5, 56);
    gettimeofday((struct timeval *) icmp->icmp_data, NULL);

    len = 8 + 56;
    icmp->icmp_cksum = 0;
    icmp->icmp_cksum = in_cksum((u_short *)icmp, len);
    printf("testing\n");
    sendto(sockfd, sendbuf, len, 0, (struct sockaddr *)tar, sizeof(struct sockaddr_in));
}


void proc_v4()
{
    char recbuf[BUFSIZE];
    //recvfrom(sockfd, &recbuf, sizeof(recbuf), 0, &target, sizeof(target));
    //printf("n = %i", n);

}









uint16_t
in_cksum(uint16_t *addr, int len)
{
    int nleft = len;
    uint32_t sum = 0;
    uint16_t *w = addr;
    uint16_t answer = 0;

    while(nleft > 1)
    {
        sum +=  *w++;
        nleft -= 2;
    }

    if(nleft == 1)
    {
        *(unsigned char *) (&answer) = *(unsigned char *)w;
        sum += answer;
    }

    sum = (sum >> 16) + (sum & 0xffff);
    sum += (sum >> 16);
    answer = ~sum;
    return(answer);
}





















