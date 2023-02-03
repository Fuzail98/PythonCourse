import telnetlib
import time

tn = telnetlib.Telnet(host='10.0.0.3', port=23)

tn.read_until(b'Username:')
tn.write(b'admin\n')
tn.read_until(b'Password:')
tn.write(b'admin\n')

tn.write(b'en\n')
tn.write(b'terminal length 0\n')
tn.write('show version\n'.encode())
tn.write(b'exit\n')

time.sleep(1)

out = tn.read_all()
out = out.decode()
print(out)
