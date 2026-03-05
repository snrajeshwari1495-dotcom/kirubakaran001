import subprocess

def block_ip(ip):
    cmd = ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]
    subprocess.run(cmd)

if __name__ == "__main__":
    block_ip("192.168.1.50")