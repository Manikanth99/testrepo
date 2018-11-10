s = """Session ID: 268917, Policy name: Intent_1/7, Timeout: 2, Valid
  In: 123.1.1.2/26 --> 157.240.24.35/928;icmp, Conn Tag: 0x0, If: ge-0/0/4.341, Pkts: 1, Bytes: 84, 
  Out: 157.240.24.35/928 --> 47.2.41.1/11377;icmp, Conn Tag: 0x0, If: ge-0/0/3.0, Pkts: 1, Bytes: 84, 

Session ID: 268918, Policy name: Intent_1/7, Timeout: 2, Valid
  In: 123.1.1.2/27 --> 157.240.24.35/928;icmp, Conn Tag: 0x0, If: ge-0/0/4.341, Pkts: 1, Bytes: 84, 
  Out: 157.240.24.35/928 --> 47.2.41.1/5765;icmp, Conn Tag: 0x0, If: ge-0/0/3.0, Pkts: 1, Bytes: 84, 

Session ID: 268919, Policy name: Intent_1/7, Timeout: 4, Valid
  In: 123.1.1.2/28 --> 157.240.24.35/928;icmp, Conn Tag: 0x0, If: ge-0/0/4.341, Pkts: 1, Bytes: 84, 
  Out: 157.240.24.35/928 --> 47.2.41.1/3553;icmp, Conn Tag: 0x0, If: ge-0/0/3.0, Pkts: 1, Bytes: 84, 
Total sessions: 3
"""

for i in s.split("\n"):
	if "Out:" in i:
		j =  i.split(':')[3].split(",")[0]
		cmd = "show configuration interfaces "+j+" | display inheritance | display set"
		break
print cmd


s1 = "set interfaces ge-0/0/3 unit 0 family inet address 47.2.41.1/24"
ip = s1.split()[-1].split('/')[0]
print ip
