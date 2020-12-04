def get_passports(lines):
    passports = list()
    d = dict()
    for li in lines:
        if not li:
            passports.append(d)
            d = dict()
        else:
            fields = li.split()
            for s in fields:
                k, v = s.split(':')
                d[k] = v
    if d:
        passports.append(d)
    return passports

def part1(passports, check_values=False):
    target_key_set = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    num_valid = 0
    for p in passports:
        if set(p.keys()).issuperset(target_key_set):
            if check_values:
                try:
                    assert_values_valid(p)
                except (AssertionError, ValueError):
                    continue
            num_valid += 1
    print(num_valid)

def assert_values_valid(d):
    #Can throw AssertionError or ValueError
    byr = int(d['byr'])
    iyr = int(d['iyr'])
    eyr = int(d['eyr'])
    hgt_raw = d['hgt']
    hgt, hgt_units = int(hgt_raw[:-2]), hgt_raw[-2:]
    hcl = d['hcl']
    ecl = d['ecl']
    pid = d['pid']

    assert 1920<=byr<=2002
    assert 2010<=iyr<=2020
    assert 2020<=eyr<=2030
    assert hgt_units in ['cm', 'in']
    if hgt_units == 'cm':
        assert 150<=hgt<=193
    else:
        assert 59<=hgt<=76
    assert len(hcl)==7 and hcl[0] == '#'
    hcl2 = int(hcl[1:], 16)
    assert ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    assert len(pid) == 9
    pid2 = int(pid)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [s.strip() for s in f.readlines()]
    passports = get_passports(lines)
    print(len(passports), 'passports found')
    part1(passports)
    part1(passports, check_values=True)

