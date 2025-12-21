#imports
import json
import os

class Host:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port

class Manager:
    def __init__(self, hosts=None, filename='hosts.json', verbose=False):
        self.filename = filename
        self.hosts = hosts if hosts is not None else []
        #load hosts json
        self.load_hosts(verbose=verbose)

    def save_hosts(self):  # ← ЭТОГО НЕ ХВАТАЕТ!
        """save hosts to json file"""
        data = [{'name': h.name, 'ip': h.ip, 'port': h.port} for h in self.hosts]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_hosts(self, verbose=False):
        """load hosts from json file"""
        if verbose: print(f"Attempting to load: {self.filename}")

        if os.path.exists(self.filename):
            if verbose: print(f"File exists, size: {os.path.getsize(self.filename)} bytes")
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if verbose: print(f"File content: {content[:100]}...")

                    f.seek(0)
                    data = json.load(f)
                    if verbose: print(f"Loaded data: {len(data)} records")

                self.hosts = [Host(d['name'], d['ip'], d['port']) for d in data]
                if verbose: print(f"Loaded hosts: {len(self.hosts)}")

            except json.JSONDecodeError as e:
                if verbose: print(f"JSON error: {e}")
            except KeyError as e:
                if verbose: print(f"Missing JSON key: {e}")
            except Exception as e:
                if verbose: print(f"Unknown error: {type(e).__name__}: {e}")
        else:
            if verbose: print("hosts.json file not found")

    def add_host(self, name, ip, port):
        host = Host(name, ip, port)
        if any(h.name == name for h in self.hosts):
            raise Exception(f"Host '{name}' already exists")
        self.hosts.append(host)
        self.save_hosts()

    def remove_host(self, name):
        initial_count = len(self.hosts)
        self.hosts[:] = [h for h in self.hosts if h.name != name]
        if len(self.hosts) < initial_count:
            print(f"Host '{name}' removed")
            self.save_hosts()  # ← Этот метод вызывается здесь
        else:
            print(f"Host '{name}' not found")

    def change_host(self, name, ip=None, port=None):
        was_updated = False

        self.hosts[:] = [
            Host(name, ip if ip is not None else h.ip, port if port is not None else h.port)
            if h.name == name else h
            for h in self.hosts
        ]

    def get_hosts(self):
        for host in self.hosts:
            print(f"  {host.name}: {host.ip}:{host.port}")
        return self.hosts

    def get_ips(self):
        return [host.ip for host in self.hosts]

    def get_host_ip(self, name):
        for host in self.hosts:
            if host.name == name:
                return host.ip
            else:
                print(f"Host '{name}' not found")

    def get_ports(self):
        return [host.port for host in self.hosts]

    def get_host_port(self, name):
        for host in self.hosts:
            if host.name == name:
                return host.port
            else:
                print(f"Host '{name}' not found")
