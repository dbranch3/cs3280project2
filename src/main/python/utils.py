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


#def validate_ip(raw_input):
#def validate_subnet(raw_input):
#def calculate_subnet(ip_address, subnet_mask):
