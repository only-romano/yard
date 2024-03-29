#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <winsock2.h>
#include <unistd.h>
#include <Ws2tcpip.h>

void error(char *msg)
{
    fprintf(stderr, "%s; %s\n", msg, strerror(WSAGetLastError()));
    exit(1);
}

int open_socket(char *host, char *port)
{
    struct addrinfo *res;
    struct addrinfo hints;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = PF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    if (getaddrinfo(host, port, &hints, &res) == -1)
        error("Cannot detect address");
    int d_sock = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    if (d_sock == -1)
        error("Cannot open socket");
    int c = connect(d_sock, res->ai_addr, res->ai_addrlen);
    freeaddrinfo(res);
    if (c == -1)
        error("Cannot connect to socket");
    return d_sock;
}

int say(int socket, char *s)
{
    int result = send(socket, s, strlen(s), 0);
    if (result == -1)
        fprintf(stderr, "%s: %s\n", "Server connection error", strerror(WSAGetLastError()));
    return result;
}

int main(int argc, char *argv[])
{
    int d_sock;
    d_sock = open_socket("en.wikipedia.org", "80");
    char buf[255];
    sprintf(buf, "GET /wiki/%s http/1.1\r\n", argv[1]);
    say(d_sock, buf);
    say(d_sock, "Host: en.wikipedia.org\r\n\r\n");
    char rec[256];
    int bytesRcvd = recv(d_sock, rec, 255, 0);
    while (bytesRcvd)
    {
        if (bytesRcvd == -1)
            error("Cannot read data sended by server");
        rec[bytesRcvd] = '\0';
        printf("%s", rec);
        bytesRcvd = recv(d_sock, rec, 255, 0);
    }
    closesocket(d_sock);
    return 0;
}
