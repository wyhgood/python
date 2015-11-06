#ifndef TCP_SYN_H
#define TCP_SYN_H
#include "netinet/in_systm.h"
#include "netinet/ip.h"
#include "netinet/ip_icmp.h"
#include "memory.h"
int nsent;
//int sockfd;
//struct sockaddr_in target;

void test();

void send_v4(int sockfd, struct sockaddr_in *target);

void proc_v4(int sockfd, struct sockaddr_in *target);
uint16_t in_cksum(uint16_t *addr, int len);



#endif
