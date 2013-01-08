#! /usr/bin/env python
# vim:ts=4:sw=4:expandtab
'''
Created on May 30, 2012

@author: mortner
'''
from scapy.all import *
import sys, logging
import ipaddr
import SimpleOptparse

conf.verb=0     #suppress verbose output
LOG = logging.getLogger("ipudpflood")

def sendUDP(src,dst,sport=0xBAAD,dport=0xF00D,padd="Fancy",times=1):
    p = Ether()/IP(src=src,dst=dst)/UDP(sport=sport,dport=dport)/(padd*times)
    sendp(p)



if __name__ == '__main__':
    optDef = {  
                (('--help',         '-h')           ,"This help"):                                              False,
                (('--verbosity',    '-v')           ,"NOTSET=0 <- Debug,Info,Warning,Error -> CRITICAL=50"):       10,
                (('--iface',         '-i')           ,"interface to use"):    'eth1',
                (('--payload-size',    '-s')           ,"payload size x times payload pattern"):  10,
                (('--payload-pattern', '-p')           ,"pattern * size = payload"):  "Fancy",               
                (('--numPackets', '-n')           ,"number of individual src-dst-IP UDP packets to spawn"):  1,   
                (('--src-net', '-x')           ,"Source Network"):  '172.16.5.0/24', 
                (('--dst-net', '-y')           ,"Destination Network"):  '172.16.6.0/24', 
        (('--dst-blacklist','-v')    ,"Blacklist Host (e.g. Gateway"): '172.16.6.1',
        (('--src-blacklist','-w')    ,"Blacklist Host (e.g. Gateway"): '172.16.5.1',
              }
    # do the magic
    options,arguments= SimpleOptparse.parseOpts(optDef)
    #cmdline defines verbosity
    LOG.setLevel(options['verbosity']) 

    conf.iface=options['iface']
    logging.info("init - ok")
    
    src = ipaddr.IPv4Network(options['src-net']).iterhosts()
    dst = ipaddr.IPv4Network(options['dst-net']).iterhosts()   

    src_blacklist = ipaddr.IPAddress(options['src-blacklist'])
    dst_blacklist = ipaddr.IPAddress(options['dst-blacklist'])

    for i in range(int(options['numPackets'])):
        src_host=src.next()
        dst_host=dst.next()

        if src_host==src_blacklist:
            src_host=src.next()
        if dst_host==dst_blacklist:
            dst_host=dst.next()
    
    
        sendUDP(str(src_host),str(dst_host),padd=options['payload-pattern'],times=options['payload-size'])
        LOG.debug("%d sent (%s <-> %s)"%(i,src_host,dst_host))
    LOG.info ("Done!")
