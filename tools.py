import ping3
import hostmanager

manager = hostmanager.Manager()

def ping_host(host):
    ip = manager.get_host_ip(host)
    if ip is None:
        return False
    result = ping3.ping(ip, timeout=5)
    if result is not None and result > 0:
        return True
    return False


def ping_hosts():
    result = {}
    for host_obj in manager.hosts:
        host = host_obj.name if hasattr(host_obj, 'name') else str(host_obj)
        ip = manager.get_host_ip(host)
        if ip is None:
            result[host] = False
            continue

        ping_result = ping3.ping(ip, timeout=5)
        result[host] = ping_result is not None and ping_result > 0
    return result

