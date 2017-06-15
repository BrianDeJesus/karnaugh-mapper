# simplify using boolean algebra
def simplify_alg(sop):
    lst = sop
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    a_count, b_count, c_count, d_count = check_for_terms(lst, a_count, b_count, c_count, d_count)
    lst = distinguish_comps(lst, a_count, b_count, c_count, d_count)
    a_count, b_count, c_count, d_count = get_counts(lst, a_count, b_count, c_count, d_count)

    if a_count != 1 and b_count != 1 and c_count != 1 and d_count != 1: #part of expression simplifiable
        if 'A' in sop:                        #simplify four group results with lone terms
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'A')
        if 'B' in sop:
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'B')
        if 'C' in sop:
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'C')
        if 'D' in sop:
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'D')
        if 'A\'' in sop:
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'A\'')
        if 'B\'' in sop:
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'B\'')
        if 'C\'' in sop:
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'C\'')
        if 'D\'' in sop:
            sop = trim_list(sop, lst, a_count, b_count, c_count, d_count, 'D\'')
        if '' in sop:
            sop.remove('')
        sop = ' + '.join(map(str, sop))
        return sop
    # account for symmetry
    elif a_count == b_count and c_count == d_count:   #whole expression simplifiable
        return simplify_symmetry(lst, a_count, b_count, c_count, d_count)
    elif a_count == c_count or b_count == d_count:
        return simplify_symmetry(lst, a_count, b_count, c_count, d_count)
    elif a_count == b_count:
        return simplify_symmetry(lst, a_count, b_count, c_count, d_count)
    elif b_count == c_count:
        return simplify_symmetry(lst, a_count, b_count, c_count, d_count)
    elif a_count == d_count and b_count == c_count:
        return simplify_symmetry(lst, a_count, b_count, c_count, d_count)
    else:
        sop = ' + '.join(map(str, sop))
        return sop

def simplify_symmetry(lst, a_count, b_count, c_count, d_count):
    lst = rm_complementary(lst, a_count, b_count, c_count, d_count)
    lst = ''.join(map(str, lst))
    if len(lst) == 0:
        return ('1')
    else:
        return lst

def flatten(lst):
    return [char for string in lst for char in string]

def trim_list(sop, lst, a_count, b_count, c_count, d_count, term):
    newer = []
    if term in sop:
        lst = list(set(lst))
        i = 0
        if 'A' in flatten(lst):
            while i < len(lst):
                if lst[i] == 'A' or lst[i] == 'A\'':
                    lst.pop(i)
                else:
                    i += 1
            if a_count == 0:
                lst.append('A\'')
            elif a_count == 2:
                lst.append('A')
        if 'B' in flatten(lst):
            i = 0
            while i < len(lst):
                if lst[i] == 'B' or lst[i] == 'B\'':
                    lst.pop(i)
                else:
                    i += 1
            if b_count == 0:
                lst.append('B\'')
            elif b_count == 2:
                lst.append('B')
        if 'C' in flatten(lst):
            i = 0
            while i < len(lst):
                if lst[i] == 'C' or lst[i] == 'C\'':
                    lst.pop(i)
                else:
                    i += 1
            if c_count == 0:
                lst.append('C\'')
            elif c_count == 2:
                lst.append('C')
        if 'D' in flatten(lst):
            i = 0
            while i < len(lst):
                if lst[i] == 'D' or lst[i] == 'D\'':
                    lst.pop(i)
                else:
                    i += 1
            if d_count == 0:
                lst.append('D\'')
            elif d_count == 2:
                lst.append('D')
        if term in lst:             #remove but append later to separate single term results
            lst.remove(term)
        lst = ''.join(map(str, lst))
        newer.append(lst)
        newer.append(term)
        return newer
    else:
        return lst

def get_counts(lst, a_count, b_count, c_count, d_count):
    for item in lst:
        if item == 'A':
            a_count += 1
        elif item == 'A\'':
            a_count -= 1
        elif item == 'B':
            b_count += 1
        elif item == 'B\'':
            b_count -= 1
        elif item == 'C':
            c_count += 1
        elif item == 'C\'':
            c_count -= 1
        elif item == 'D':
            d_count += 1
        elif item == 'D\'':
            d_count -= 1
    return a_count, b_count, c_count, d_count

#check and initialize variable appearance
def check_for_terms(lst, a_count, b_count, c_count, d_count):
    lst = [char for string in lst for char in string]
    if 'A' in lst:
        a_count = 1
    if 'B' in lst:
        b_count = 1
    if 'C' in lst:
        c_count = 1
    if 'D' in lst:
        d_count = 1
    return a_count, b_count, c_count, d_count

# separate each char
def distinguish_comps(lst, a_count, b_count, c_count, d_count):
    new_lst = []
    lst = flatten(lst)
    for i in range(1, len(lst)):
        if lst[i] == '\'' and lst[i-1] == 'A':
            new_lst.append('A\'')
        elif lst[i] == '\'' and lst[i-1] == 'B':
            new_lst.append('B\'')
        elif lst[i] == '\'' and lst[i-1] == 'C':
            new_lst.append('C\'')
        elif lst[i] == '\'' and lst[i-1] == 'D':
            new_lst.append('D\'')
    i = 0
    while i < len(lst):
        if lst[i] == 'A' and lst[(i + 1) % len(lst)] != '\'':
            new_lst.append('A')
        if lst[i] == 'B' and lst[(i + 1) % len(lst)] != '\'':
            new_lst.append('B')
        if lst[i] == 'C' and lst[(i + 1) % len(lst)] != '\'':
            new_lst.append('C')
        if lst[i] == 'D' and lst[(i + 1) % len(lst)] != '\'':
            new_lst.append('D')
        i += 1
    return new_lst
#simplify term complements
def rm_complementary(lst, a_count, b_count, c_count, d_count):
    new_lst = distinguish_comps(lst, a_count, b_count, c_count, d_count)
    i = 0
    while i < len(new_lst):
        if (new_lst[i] == 'A' or new_lst[i] == 'A\'') and a_count == 1:
            new_lst.pop(i)
        elif (new_lst[i] == 'B' or new_lst[i] == 'B\'') and b_count == 1:
            new_lst.pop(i)
        elif (new_lst[i] == 'C' or new_lst[i] == 'C\'') and c_count == 1:
            new_lst.pop(i)
        elif (new_lst[i] == 'D' or new_lst[i] == 'D\'') and d_count == 1:
            new_lst.pop(i)
        else:
            i += 1
    return list(set(new_lst))
