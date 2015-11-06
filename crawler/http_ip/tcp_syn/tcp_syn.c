#include "tcp_syn.h"
#include "stdio.h"
#include "sys/socket.h"
#include "netdb.h"
#include "netinet/in.h"
#include <sys/types.h>



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
    int addrlen = sizeof(struct sockaddr_in);
    sendto(sockfd, sendbuf, len, 0, (struct sockaddr *)tar, addrlen);
    return;
}


void recv_v4(int sockfd, struct sockaddr_in *tar)
{
    bzero(recvbuf,sizeof(recvbuf));
    int len = sizeof(struct sockaddr_in);
    int n = recvfrom(sockfd, recvbuf, sizeof(recvbuf), 0, (struct sockaddr *)tar, &len);
    printf("n = %i\n", n);
    return;
}


void
proc_v4()
{
    printf("-2-2-2-2-\n");
    
    int hlen, icmplen;
    int len = 84;
    //int len = sizeof(recvbuf);
    printf("recvlen\t%i", len);
    double rtt;
    struct ip ip;
    
    printf("-1-1-1-1-1-1");
    
    
    struct icmp *icmp;
    //struct timeval *tvsend;
    printf("00000000000");
    
    struct ip *ip_tmp  = (struct ip *)&recvbuf;
    ip = *ip_tmp;
    printf("1111111111111");
   

 
    printf("hlen\t%i\n", hlen);
    if(ip.ip_p != IPPROTO_ICMP)
        return ;
    icmp = (struct icmp *) (&recvbuf + hlen);
    if((len -= hlen) < 8)
	return;
    struct icmp icmp_tmp = *icmp;
    int flag = icmp_tmp.icmp_type == ICMP_ECHOREPLY;
    
    printf("flag\t %i", flag);
    int pid = icmp_tmp.icmp_id;
    printf("pid\t %i\n", pid);
    if(icmp_tmp.icmp_type == ICMP_ECHOREPLY)
    
    if(icmp_tmp.icmp_id != getpid())
    	return;

       // tvsend = (struct timeval *) icmp->icmp_data;
        //tv_sub(tvrecv, tvsend);
        //rtt = tvrecv->tv_sec * 1000.0 + tvrecv->tv_usec /1000.0;
    printf("  null bytes from : type = %d, code = %d\n",icmp_tmp.icmp_type, icmp_tmp.icmp_code);
    
	
    
    return;
}

void
tv_sub(struct timeval *out, struct timeval *in)
{
    if((out->tv_usec -= in->tv_usec) < 0)
    {
        --out->tv_sec;
        out->tv_usec += 1000000;
    }
    out->tv_sec -= in->tv_sec;
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





















