import re

def is_ipv4(raw_input):
    if (raw_input == None):
        raise ValueError("Input cannot be none")

    output = True
    ipv4_regex = re.compile(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$')
    matched = ipv4_regex.match(raw_input)
    
    if matched == None:
        output = False

    return output

def is_ipv6(raw_input):
    if (raw_input == None):
        raise ValueError("Input cannot be none")

    output = True
    expanded_ipv6_address = expand_ipv6_address(raw_input)
    ipv6_regex = re.compile(r'^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$')
    matched = ipv6_regex.match(expanded_ipv6_address)

    if matched == None:
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

def expand_ipv6_address(ip_address):
    ip_address_with_placeholder = ip_address.replace("::", ":zeroes:", 1)
    segments = ip_address_with_placeholder.split(":")
    expanded_segments = []

    while "" in segments: segments.remove("")

    for i in range(len(segments)):
        current_segment = segments[i]
        new_segment = get_segment_with_leading_zeroes(current_segment)
        expanded_segments.append(new_segment)
            
    num_zero_groups_missing = 8 - len(expanded_segments)

    for i in range(len(expanded_segments)):
        if expanded_segments[i] == "zeroes":
            replacement_segment = "0000"
            for j in range(num_zero_groups_missing):
                replacement_segment = replacement_segment + ":0000"
            expanded_segments[i] = replacement_segment

    return ":".join(expanded_segments)

def get_segment_with_leading_zeroes(original_segment):
    output_segment = ""
    if len(original_segment) < 4:
        num_leading_zeroes = 4 - len(original_segment)

        for i in range(num_leading_zeroes):
            output_segment = output_segment + "0"

    output_segment = output_segment + original_segment

    return output_segment

def get_ipv6_subnet_mask(prefix_length):
    mask = ""
    for i in range(0, prefix_length, 4):
        mask = mask + "F"
        
    for i in range(prefix_length, 128, 4):
        mask = mask + "0"

    grouping = [(mask[i:i+4]) for i in range(0, len(mask), 4)]

    return ":".join(grouping)
    
#def calculate_subnet_ipv6(ip_address, prefix_length):
    #ipv6_mask = get_ipv6_subnet_mask(prefix_length)

