import socket
import dns.resolver
import whois

def gather_website_info(url):
    result = []
    hostname = url.replace("https://", "").replace("http://", "").split('/')[0]
    
    result.append(f"Checking website: {hostname}")

    # Get IP Address
    try:
        ip = socket.gethostbyname(hostname)
        result.append(f"IP Address: {ip}")
    except socket.gaierror:
        result.append("Error: Hostname could not be resolved.")
    except Exception as e:
        result.append(f"Error fetching IP address: {e}")
    
    # Get DNS Records
    dns_info = []
    
    try:
        a_records = dns.resolver.resolve(hostname, 'A')
        dns_info.append(f"DNS Info for {hostname}:")
        for ipval in a_records:
            dns_info.append(f"A Record: {ipval.to_text()}")
    except Exception as e:
        dns_info.append(f"Error fetching A Record: {e}")

    try:
        mx_records = dns.resolver.resolve(hostname, 'MX')
        for mx in mx_records:
            dns_info.append(f"MX Record: {mx.exchange} with preference {mx.preference}")
    except Exception as e:
        dns_info.append(f"Error fetching MX Record: {e}")

    try:
        ns_records = dns.resolver.resolve(hostname, 'NS')
        for ns in ns_records:
            dns_info.append(f"NS Record: {ns.to_text()}")
    except Exception as e:
        dns_info.append(f"Error fetching NS Record: {e}")

    try:
        txt_records = dns.resolver.resolve(hostname, 'TXT')
        for txt in txt_records:
            dns_info.append(f"TXT Record: {txt.to_text()}")
    except Exception as e:
        dns_info.append(f"Error fetching TXT Record: {e}")

    result.extend(dns_info)

    # Get WHOIS Information
    try:
        domain_info = whois.whois(hostname)
        whois_info = [
            "\nWHOIS Information:",
            f"Domain Name: {domain_info.domain_name}" if domain_info.domain_name else "Domain Name: Not Available",
            f"Registrar: {domain_info.registrar}" if domain_info.registrar else "Registrar: Not Available",
            f"Creation Date: {domain_info.creation_date}" if domain_info.creation_date else "Creation Date: Not Available",
            f"Expiration Date: {domain_info.expiration_date}" if domain_info.expiration_date else "Expiration Date: Not Available",
            f"Nameservers: {domain_info.name_servers}" if domain_info.name_servers else "Nameservers: Not Available",
            f"Status: {domain_info.status}" if domain_info.status else "Status: Not Available"
        ]
        result.extend(whois_info)
    except Exception as e:
        result.append(f"Error fetching WHOIS info: {e}")
    
    # Ensure function always returns exactly two values
    message = '\n'.join(result) if result else "No Details Found"
    return 200, message
