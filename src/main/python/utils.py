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

#def validate_ip(raw_input):
#def validate_subnet(raw_input):
#def calculate_subnet(ip_address, subnet_mask):
