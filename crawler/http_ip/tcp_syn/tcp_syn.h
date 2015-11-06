#ifndef TCP_SYN_H
#define TCP_SYN_H
#include "netinet/in_systm.h"
#include "netinet/ip.h"
#include "netinet/ip_icmp.h"
#include "memory.h"

#define BUFSIZE 1500
int nsent;
//int sockfd;
//struct sockaddr_in target;

char recvbuf[BUFSIZE];
void test();

void send_v4(int sockfd, struct sockaddr_in *target);

void recv_v4(int sockfd, struct sockaddr_in *target);

void proc_v4();
void tv_sub(struct timeval *, struct timeval *);

uint16_t in_cksum(uint16_t *addr, int len);



#endif
