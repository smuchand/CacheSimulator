def trace_handler(cache_model, filename):
    address = []
    access_type = []
    with open(filename) as file:
        lines = file.readlines()

        for i in range(len(lines)):
            address.append(lines[i].split()[1])
            access_type.append(lines[i].split()[0])

    if cache_model == '0':
        return address

    else:
        return access_type, address
