
A fair distribution algorithm in python to spread different services with different weights in different nodes  

i had this problem some days ago while designign my new monitoring system
we have X service to monitor and each of them has a specific weight to monitor
weight as in how much CPU/Network/IO would spend to monitor
and the number of service had to be eavenly distributed in N servers that would
server as monitors
so I wrote a solution for my problem and thought it might come in help somebody
1 - we sum the weights of our services
2 - we get the ratio ( sum_of_weighs/nr_of_servers_we_have_to_do_checks)
3 - we sort according to the heaviest
4 - start a card like distribution but when someone reaches we will skip him
nr i nyjeve N
index weight type
0 1 ping
1 2 pop_check
2 2 smtp_check
3 2 blacklist
4 3 http_status
5 3 http_content
6 3 http_title
7 10 http_load
we get the services ( randomly generated )
(0, 3)
(1, 2)
(2, 3)
(3, 10)
(4, 10)
(5, 3)
(6, 2)
(7, 2)
i rendisim
(1, 2)
(6, 2)
(7, 2)
(0, 3)
(2, 3)
(5, 3)
(3, 10)
(4, 10)
llogarisim shprendarjen per N=3 nyje
totali 6 + 9 + 20 = 35
35 / 3 = 11.6 =~ 12
nyja e fundit ose do kete pak me shume/pak
target: (varianti 1)
13 13 9
--------------------------------
duke nisur qe nga fundit heqim te medhajat
dhe shprendajme
10 10 3
3 3 3
- - 2
- - 2
--------------------------------
13 13 9
DONE
target: (varianti 2)
12 12 11
--------------------------------
10 10 3
3 3 3
- - 2
- - 2
--------------------------------
13 13 9
DONE
