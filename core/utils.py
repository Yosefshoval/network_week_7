import re

def input_addresses():
    ip = input('Enter your ip address: ')
    mask = input('Enter mask: ')
    return ip, mask



def validate_addresses(address : str, addr_type : str): # addr_type = 'ip' or 'mask'
    if '.' not in address:
        return f'{address}: This is invalid ip address'

    if addr_type == 'ip' and address in ['0.0.0.0', '255.255.255.255']:
        return f"{address}: This ip not able to be a device's ip"

    splitted_address = address.split('.')
    if len(splitted_address) != 4:
        return 'This address not include 4 octets'

    flag = False
    for i, octet in enumerate(splitted_address):
        if not octet.isdigit() or int(octet) > 255:
            return f'{address}: This is invalid ip address'
        if flag and octet != '0':
            return f'The octet {i + 1} must be 0'
        if octet == '0':
            flag = True

    return True



def calc_network_address(ip, mask):
    splitted_ip = ip.split('.')
    splitted_mask = mask.split('.')

    network_address = [str( int( splitted_ip[octet] ) & int(splitted_mask[octet] ) ) + '.' for octet in range(4)]

    return ''.join(network_address)[:-1]
# print(calc_network_address('192.168.10.5', '255.255.0.0'))




def calc_broadcast_address(network : str, hosts_num : int, mask : str):
    pass


def calc_hosts_number(cidr):
    return 2 ** (32 - cidr) - 2




def detect_class_kind(mask):
    splitted_mask = mask.split('.')
    for octet in range(4):
        if splitted_mask[octet] not in ['255', '0']:
            return 'Classless'
        if splitted_mask[octet] == '0':
            match octet:
                case 1:
                    return 'class A'
                case 2:
                    return 'class B'
                case 3:
                    return 'class C'
    return False





def string_output(ip, mask, class_type, network_address, broadcast_address, hosts_number, cidr):
    result = f"""
Input IP: {ip}
Subnet Mask: {mask}
{class_type}
Network Address: {network_address}
Broadcast Address: {broadcast_address}
Number of Hosts in this subnet: {hosts_number}
CIDR Mask: {cidr}
"""
    return result



def insert_result_to_file(file, result):
    try:
        with open(file, 'w') as f:
            f.write(result)
            return 'Saved successfully'
    except Exception as e:
        return f'Error: {e}'
