import core.utils as ut


def main():
    while True:
        ip, mask = ut.input_addresses()
        if not ut.validate_addresses(ip, 'ip') or not ut.validate_addresses(mask, 'mask'):
            print('invalid input. try again please.')
            continue

        net_address = ut.calc_network_address(ip, mask)
        cidr = ut.detect_cidr(mask)

        hosts_num = ut.calc_hosts_number(cidr)
        broadcast = ut.calc_broadcast_address(net_address, cidr, mask)

        class_type = ut.detect_class_kind(mask)

        result = ut.string_output(ip, mask, class_type, net_address, broadcast, hosts_num, cidr)
        is_saved = ut.insert_result_to_file(f'subnet_info_[{net_address}]_[{my_id}].txt', result)

        print(is_saved)



if __name__ == '__main__':
    main()