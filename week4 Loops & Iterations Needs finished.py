# Week 4: Loops and Iteration
# Goal: Identify internal vs external IP addresses

ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]

for ip in ip_addresses:
    print(ip)

for ip in ip_addresses:
    if ip.startswith("192.168.") or ip.startswith("10."):
        print(f"{ip} is an internal address.")
    else:
        print(f"{ip} is an external address.")

for ip in ip_addresses:
    if ip.startswith("192.168."):
        zone = "Private (Class C)"
    elif ip.startswith("10."):
        zone = "Private (Class A)"
    elif ip.startswith("172.16.") or ip.startswith("172.17.") or ip.startswith("172.31."):
        zone = "Private (Class B)"
    else:
        zone = "Public"

    print(f"{ip} → {zone}")

internal_count = 0
external_count = 0

for ip in ip_addresses:
    if ip.startswith(("192.168.", "10.", "172.")):
        internal_count += 1
    else:
        external_count += 1

print(f"Internal: {internal_count}")
print(f"External: {external_count}")

Enter an IP (or 'done' to finish): 192.168.2.5
192.168.2.5 is internal.
Enter an IP (or 'done' to finish): 8.8.8.8
8.8.8.8 is external.
Enter an IP (or 'done' to finish): done

with open("ips.txt") as f:
    ip_addresses = f.read().splitlines()

internal_ips = []

for ip in ip_addresses:
    if ip.startswith(("192.168.", "10.")):
        internal_ips.append(ip)

with open("internal_ips.txt", "w") as out:
    for ip in internal_ips:
        out.write(ip + "\n")

