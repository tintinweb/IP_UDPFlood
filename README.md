IP_UDPFlood
===========

General purpose IP src/dst network flooder

Dependencies: [SimpleOptparse](https://github.com/tintinweb/LegacyOptparse/), [ipaddr](http://code.google.com/p/ipaddr-py/)  


Example
-------

	Usage: ip_udp_netflood.py  [OPTIONS] [Argument(s) ...]
	
	Mandatory arguments to long options are mandatory for short options too.
	
	  -x <value>, --src-net=<value>              Source Network.
	                                             *** DEFAULT='172.16.5.0/24'
	  -n <value>, --numPackets=<value>           number of individual src-dst-IP UDP packets to spawn.
	                                             *** DEFAULT='1'
	  -i <value>, --iface=<value>                interface to use.
	                                             *** DEFAULT='eth1'
	  -p <value>, --payload-pattern=<value>      pattern * size = payload.
	                                             *** DEFAULT='Fancy'
	  -v <value>, --verbosity=<value>            NOTSET=0 <- Debug,Info,Warning,Error -> CRITICAL=50.
	                                             *** DEFAULT='10'
	  -y <value>, --dst-net=<value>              Destination Network.
	                                             *** DEFAULT='172.16.6.0/24'
	  -h,         --help                         This help.
	  -s <value>, --payload-size=<value>         payload size x times payload pattern.
	                                             *** DEFAULT='10'
	  -w <value>, --src-blacklist=<value>        Blacklist Host (e.g. Gateway.
	                                             *** DEFAULT='172.16.5.1'
	  -v <value>, --dst-blacklist=<value>        Blacklist Host (e.g. Gateway.
	                                             *** DEFAULT='172.16.6.1'


