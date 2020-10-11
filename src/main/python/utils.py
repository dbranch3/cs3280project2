import re

def is_ipv4(raw_input):
    if (raw_input == None):
        raise ValueError("Input cannot be none")

    output = True
    ipv4_regex = re.compile(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$')
    matched = ipv4_regex.match(raw_input)
    
    if (matched == None):
        output = False

    return output

def is_valid_subnet_mask(raw_input):
    if (raw_input == None):
        raise ValueError("Input cannot be none")

    output = False
    is_ip_notation = is_ipv4(raw_input)
    int_value = int(raw_input.replace(".", "")) 

    if (int_value <= 32):
        output = True

    if (is_ip_notation):
        output = True

    return output

def calculate_subnet_ipv4(ip_address, subnet_mask):
    ipv4_regex = re.compile(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$')
    ip_segments = ipv4_regex.findall(ip_address)[0]
    subnet_mask_segments = ipv4_regex.findall(subnet_mask)[0]
    binary_subnet_segments = []

    for i in range(4):
        integer_ip_segment = int(ip_segments[i])
        integer_subnet_segment = int(subnet_mask_segments[i])
        result_of_AND_operation = integer_ip_segment & integer_subnet_segment
        string_form = str(result_of_AND_operation)
        binary_subnet_segments.append(string_form)

    string_representation = ".".join(binary_subnet_segments)

    return string_representation
