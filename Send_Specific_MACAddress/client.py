import socket
import struct
import os
import fcntl


def get_mac_address(interface):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        info = fcntl.ioctl(
            sock.fileno(), 0x8915, struct.pack("256s", bytes(interface[:15], "utf-8"))
        )
        mac = ":".join(["{:02x}".format(b) for b in info[18:24]])
        return mac
    except Exception as e:
        print(e)
        return None


def get_source_mac(interface):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mac = get_mac_address(interface)
        return mac
    except Exception as e:
        print(e)
        return None


def get_destination_mac(destination_ip):
    try:
        # Check if destination_ip is valid IP address
        socket.inet_aton(destination_ip)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((destination_ip, 0))
        source_mac = get_mac_address(destination_ip)
        return source_mac
    except Exception as e:
        print(e)
        return None


def send_message(destination_ip, source_mac, destination_mac):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        icmp_type = 8  # 8 is ICMP type echo request
        icmp_code = 0  # always 0
        icmp_checksum = 0  # leave this as 0 for kernel to auto calculate checksum
        id_seq = 1  # Identifier and sequence number can be anything
        sequence = 1
        echo_msg = b"Echo Request Message"
        msg = struct.pack(
            "!BBHHH32s", icmp_type, icmp_code, icmp_checksum, id_seq, sequence, echo_msg
        )
        checksum = calculate_checksum(msg)
        msg = struct.pack(
            "!BBHHH32s", icmp_type, icmp_code, checksum, id_seq, sequence, echo_msg
        )
        sock.sendto(msg, (destination_ip, 0))
    except Exception as e:
        print(e)
        return None


def calculate_checksum(msg):
    s = 0
    msg = msg.encode("utf-8")
    for i in range(0, len(msg) - 1, 2):
        w = (msg[i] << 8) + msg[i + 1]
        s = s + w
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    return s


destination_ip = "localhost"
interface = "en0"
source_mac = get_source_mac(interface)
destination_mac = get_destination_mac(destination_ip)

send_message(destination_ip, source_mac, destination_mac)
