# Lab-8
This lab is an analysis of different packets sent and recieved during `ping` and `traceroute`

## Ping
The Cloudflare DNS server (1.1.1.1) was pinged and the packets exchanged were captured. Images along with captured packets can be found in the directory `ping-cap`

## Traceroute
A `traceroute` was attempted to the cloudflare DNS server (1.1.1.1), however it seems that they have disabled the ICMP request for it. Hence, `traceroute` to Google's DNS server (8.8.8.8) was executed. The images along with captured packets can be found in the directory `traceroute-cap`