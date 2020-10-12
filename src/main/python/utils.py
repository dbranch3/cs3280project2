"""
This module provides utility methods for calculating subnets and validating ip addresses
"""
import re

def ip_and_subnet_are_valid(query):
    """ Returns True if query is valid """
    output = True
    ip_address = query[0]
    subnet_mask = query[1]

    ip_version = get_ip_version(ip_address)

    if ip_version is None:
        output = False
    else:
        if ip_version == "IPV4":
            output = is_valid_subnet_mask_ipv4(subnet_mask)
        elif ip_version == "IPV6":
            output = is_valid_subnet_mask_ipv6(subnet_mask)

    return output

def get_network_address(query):
    """ Returns network address for valid query """
    ip_address = query[0]
    subnet_mask = query[1]
    ip_version = get_ip_version(ip_address)

    output = ""

    if ip_version == "IPV4":
        output = calculate_subnet_ipv4(ip_address, subnet_mask)
    elif ip_version == "IPV6":
        output = calculate_subnet_ipv6(ip_address, subnet_mask)

    return output

def is_ipv4(raw_input):
    """
    Returns True if the input is a valid IPV4 address.
    """
    output = True
    ipv4_regex = re.compile(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$')
    matched = ipv4_regex.match(raw_input)

    if matched is None:
        output = False

    return output

def is_ipv6(raw_input):
    """
    Returns True if the input is a valid IPV6 address.
    """
    output = True
    expanded_ipv6_address = expand_ipv6_address(raw_input)
    ipv6_regex = re.compile(r'^(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}$')
    matched = ipv6_regex.match(expanded_ipv6_address)

    if matched is None:
        output = False

    return output

def get_ip_version(raw_input):
    """
    Returns the version of the input IP address.
    Options are 'IPV4', 'IPV6', or 'None'
    """
    output = None

    if is_ipv4(raw_input):
        output = "IPV4"
    elif is_ipv6(raw_input):
        output = "IPV6"

    return output

def is_valid_subnet_mask_ipv4(raw_input):
    """ Returns True if the input is a valid IPV4 Subnet Mask """
    if raw_input is None:
        raise ValueError("Input cannot be none")

    output = False
    netmask_regex = re.compile(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$')
    is_netmask = netmask_regex.match(raw_input)
    int_value = int(raw_input.replace(".", ""))

    if 0 <= int_value <= 32 :
        output = True

    elif is_netmask:
        output = True

    return output

def is_valid_subnet_mask_ipv6(raw_input):
    """ Returns True if the input is a valid IPV6 Prefix length """
    if raw_input is None:
        raise ValueError("Input cannot be none")

    value = int(raw_input)
    output = False

    if 0 <= value <= 128:
        output = True

    return output

def expand_ipv6_address(ip_address):
    """ Returns the input IP address with 8 segments fully padded with zeroes """
    ip_address_with_placeholder = ip_address.replace("::", ":zeroes:", 1)
    segments = ip_address_with_placeholder.split(":")
    expanded_segments = []

    while "" in segments:
        segments.remove("")

    for seg in enumerate(segments):
        current_segment = seg[1]
        new_segment = get_segment_with_leading_zeroes(current_segment)
        expanded_segments.append(new_segment)

    num_zero_groups_missing = 8 - len(expanded_segments)

    for seg in enumerate(expanded_segments):
        if seg[1] == "zeroes":
            replacement_segment = "0000"
            for _ in range(num_zero_groups_missing):
                replacement_segment = replacement_segment + ":0000"
            expanded_segments[seg[0]] = replacement_segment

    return ":".join(expanded_segments)

def get_segment_with_leading_zeroes(original_segment):
    """ Pads an IPV6 Segment with zeroes """
    output_segment = ""
    if len(original_segment) < 4:
        num_leading_zeroes = 4 - len(original_segment)

        for _ in range(num_leading_zeroes):
            output_segment = output_segment + "0"

    output_segment = output_segment + original_segment

    return output_segment

def get_ipv6_subnet_mask(prefix_length):
    """ Generates a subnet mask for IPV6 prefix length """
    prefix_length = int(prefix_length)
    mask = ""
    for i in range(0, prefix_length, 4):
        mask = mask + "F"

    for i in range(prefix_length, 128, 4):
        mask = mask + "0"

    grouping = [(mask[i:i+4]) for i in range(0, len(mask), 4)]

    return ":".join(grouping)

def calculate_subnet_ipv4(ip_address, subnet_mask):
    """ Returns Network Address for given IP and Subnet Mask """
    ipv4_regex = re.compile(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$')
    ip_segments = ipv4_regex.findall(ip_address)[0]
    subnet_mask_segments = ipv4_regex.findall(subnet_mask)[0]
    binary_subnet_segments = []

    for i in range(4):
        integer_ip_segment = int(ip_segments[i])
        integer_subnet_segment = int(subnet_mask_segments[i])
        result_of_and_operation = integer_ip_segment & integer_subnet_segment
        string_form = str(result_of_and_operation)
        binary_subnet_segments.append(string_form)

    string_representation = ".".join(binary_subnet_segments)

    return string_representation

def calculate_subnet_ipv6(ip_address, prefix_length):
    """ Returns Network Address for given IP and Prefix Length """
    expanded_ipv6_address = expand_ipv6_address(ip_address)
    ipv6_mask = get_ipv6_subnet_mask(prefix_length)
    ipv6_mask_segments = ipv6_mask.split(":")
    ip_segments = expanded_ipv6_address.split(":")
    network_portion_segments = []

    for i in range(8):
        integer_ip_segment = int(ip_segments[i], 16)
        integer_subnet_segment = int(ipv6_mask_segments[i], 16)
        result_of_and_operation = integer_ip_segment & integer_subnet_segment
        hex_form = hex(result_of_and_operation)
        string_form = str(hex_form).replace("0x", "", 1)
        network_portion_segments.append(string_form)

    string_representation = expand_ipv6_address(":".join(network_portion_segments))

    return string_representation
