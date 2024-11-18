def register_files(files):
    mapped = {}
    for f in files:
        if len(f) > 2:
            mapped[f[0]] = {'address': [f[0]], 'size': f[1], 'children': f[2:]}
        else:
            mapped[f[0]] = {'address': [f[0]], 'size': f[1], 'children': None}
    return mapped

def add_parent(file, mapped):
    if mapped[file]['children']:
        for child in mapped[file]['children']:
            for f in mapped[file]['address']:
                if f not in mapped[child]['address']:
                    mapped[child]['address'].append(f)
            add_parent(child, mapped)

def map_files(files):
    mapped = register_files(files)
    for f in files:
        if len(f) > 2:
            add_parent(f[0], mapped)
    return mapped

def get_top_file(dct):
    dct = sorted(dct.values(), key=lambda x: len(x['address']))
    return dct[0]['address'][0]

def get_size(file, mapped, size={}):
    if file not in size:
        size[file] = mapped[file]['size']
    if mapped[file]['children']:
        for child in mapped[file]['children']:
            if child not in size:
                size[file] += get_size(child, mapped, size)
            else:
                size[file] += size[child]
    else:
        size[file] = mapped[file]['size']
    return size[file]

def balancing(top, mapped, sizes):
    children_sizes = {child: sizes[child] for child in mapped[top]['children']}
    if len(set(children_sizes.values())) == 1:
        unbalanced = top
        unbalanced_size = mapped[unbalanced]['size']
        compare_sizes = {sizes[child] for child in mapped[mapped[unbalanced]['address'][1]]['children']}
        balanced_size = unbalanced_size - (max(compare_sizes) - min(compare_sizes))
        return balanced_size
    children_sizes = sorted(children_sizes, key=lambda x: children_sizes[x], reverse=True)
    top = children_sizes[0]
    return balancing(top, mapped, sizes)


if __name__ == '__main__':
    with open('day07.txt') as f:
        files = f.read().strip()
        patterns = {'(', ')', '-> ', ','}
        for p in patterns:
            files = files.replace(p, '')
        files = [[int(i) if i.isdigit() else i for i in j.split()] for j in files.split('\n')]

    file_system = map_files(files)
    sizes = {}
    top = get_top_file(file_system)
    print( 'Part 1: ',top)
    get_size(top, file_system, sizes)
    print('Part 2: ',balancing(top, file_system, sizes))
