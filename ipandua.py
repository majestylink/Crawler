from itertools import islice
from random import choice, randint

def get_ua():
		uafile = open( "res/useragents.txt" , "r" )
		uas = uafile.read().split("\n")
		chosen = choice(uas)
		return {'User-Agent': chosen }

def get_ip():
		ipfile = open( "res/canadaip.txt" , "r" )
		ips = ipfile.read().split("\n")
		chosen = choice(ips)
		return {'http':'http://' + chosen }
