    
class portDetection:
    def port_scan_callback(self, pkt):
        if "IP" in pkt and "TCP" in pkt:
            src_ip = pkt.ip.src
            dst_ip = pkt.ip.dst
            dst_port = int(pkt.tcp.dstport)

            if dst_ip == self.target_ip:
                if src_ip not in self.scanned_ports:
                    self.scanned_ports[src_ip] = [dst_port]
                else:
                    if dst_port - 1 not in self.scanned_ports[src_ip]:
                        self.scanned_ports[src_ip].append(dst_port)
                        return True
                    else:
                        return False