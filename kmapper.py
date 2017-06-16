
#Boolean expression simplifier using kmap procedure
from input_getter import get_input
from kmap_init import BuildMap
from bool_algebra import simplify_alg

def display_format(sop):
    sop = simplify_alg(sop)    #simplify algebra expression
    print("\nSum of products: {}" .format(sop))

#vertical pairs
def get_vert_pairs(table, columns, i):
    vert_pairs = []
    if len(table) == 4:
        if columns[i] == 0:
            vert_pairs.append('B\'')
        elif columns[i] == 1:
            vert_pairs.append('B')
    elif len(table) == 8:
        if columns[i] == '11':
            vert_pairs.append('BC')
        elif columns[i] == '00':
            vert_pairs.append('B\'C\'')
        elif columns[i] == '01':
            vert_pairs.append('B\'C')
        elif columns[i] == '10':
            vert_pairs.append('BC\'')
    elif len(table) == 16:
        if i < 4:                   # covers rows 1 and 2
            if columns[i] == '11':
                vert_pairs.append('A\'CD')
            elif columns[i] == '00':
                vert_pairs.append('A\'C\'D\'')
            elif columns[i] == '01':
                vert_pairs.append('A\'C\'D')
            elif columns[i] == '10':
                vert_pairs.append('A\'CD\'')
        elif i >= 4 and i < 8:      #covers rows 2 and 3
            i %= 4
            if columns[i] == '11':
                vert_pairs.append('BCD')
            elif columns[i] == '00':
                vert_pairs.append('BC\'D\'')
            elif columns[i] == '01':
                vert_pairs.append('BC\'D')
            elif columns[i] == '10':
                vert_pairs.append('BCD\'')
        elif i >= 8 and i < 12:     # covers rows 3 and 4
            i %= 4
            if columns[i] == '11':
                vert_pairs.append('ACD')
            elif columns[i] == '00':
                vert_pairs.append('AC\'D\'')
            elif columns[i] == '01':
                vert_pairs.append('AC\'D')
            elif columns[i] == '10':
                vert_pairs.append('ACD\'')
        elif i >= 12 and i < 16:     # covers rows 4 and 1
            i %= 4
            if columns[i] == '11':
                vert_pairs.append('B\'CD')
            elif columns[i] == '00':
                vert_pairs.append('B\'C\'D\'')
            elif columns[i] == '01':
                vert_pairs.append('B\'C\'D')
            elif columns[i] == '10':
                vert_pairs.append('B\'CD\'')
    return ','.join(map(str, vert_pairs))

#groups of 4
def has_four_group(table, i):
    if len(table) == 4:
        if table[0] == table[1] == table[2] == table[3] == 1:
            return True
    if len(table) == 8:
        if i == 0:
            if table[i] == table[i+1] == table[i+3] == table[i+2] == 1:
                return True
        if i < 3:
            if table[i] == table[(i + 1) % 4] == table[i + 4] == table[i + 5] == 1:
                return True
        if i == 3:
            if table[i] == table[(i + 1) % 4] == table[i + 4] == table[4] == 1:
                return True
        if i == 4:
            if table[i] == table[i+1] == table[i+3] == table[i+2] == 1:
                return True
    elif len(table) == 16:
        if i < 4:
            if table[i] == 1 and table[(i + 1) % 4] == 0 and table[i + 12] == 0 and table[(i - 1) % 4] == 0 and table[i + 4] == 0:
                return True
        elif i >= 4 and i < 8:
            if table[i] == 1 and table[((i + 1) % 4) + 4] == 0 and table[((i - 1) % 4) + 4] == 0 and table[i + 4] == 0 and table[i - 4] == 0:
                return True
        elif i >= 8 and i < 12:
            if table[i] == 1 and table[((i + 1) % 4) + 8] == 0 and table[((i - 1) % 4) + 8] == 0 and table[i + 4] == 0 and table[i - 4] == 0:
                return True
        elif i >= 12 and i < 16:
            if table[i] == 1 and table[((i + 1) % 4) + 12] == 0 and table[((i - 1) % 4) + 12] == 0 and table[i - 12] == 0 and table[i - 4] == 0:
                return True
#unpairable
def has_no_pair(table, i):
    if len(table) == 4:
        if i == 0:
            if table[i] == 1 and table[(i+1)] == 0 and table[i+2] == 0:
                return True
        if i == 1:
            if table[i] == 1 and table[(i-1)] == 0 and table[i+2] == 0:
                return True
        if i == 2 :
            if table[i] == 1 and table[i+1] == 0 and table[i-2] == 0:
                return True
        if i == 3:
            if table[i] == 1 and table[i-1] == 0 and table[i-2] == 0:
                return True
    elif len(table) == 8:
        if i >=4 and i <=7:
            if table[i] == 1 and table[((i + 1) % 4) + 4] == 0 and table[i - 4] == 0 and table[((i - 1) % 4) + 4] == 0:
                return True
        elif i < 4:
            if table[i] == 1 and table[(i + 1) % 4] == 0 and table[i + 4] == 0 and table[(i - 1) % 4] == 0:
                return True
    elif len(table) == 16:
        if i < 4:
            if table[i] == 1 and table[(i + 1) % 4] == 0 and table[i + 12] == 0 and table[(i - 1) % 4] == 0 and table[i + 4] == 0:
                return True
        elif i >= 4 and i < 8:
            if table[i] == 1 and table[((i + 1) % 4) + 4] == 0 and table[((i - 1) % 4) + 4] == 0 and table[i + 4] == 0 and table[i - 4] == 0:
                return True
        elif i >= 8 and i < 12:
            if table[i] == 1 and table[((i + 1) % 4) + 8] == 0 and table[((i - 1) % 4) + 8] == 0 and table[i + 4] == 0 and table[i - 4] == 0:
                return True
        elif i >= 12 and i < 16:
            if table[i] == 1 and table[((i + 1) % 4) + 12] == 0 and table[((i - 1) % 4) + 12] == 0 and table[i - 12] == 0 and table[i - 4] == 0:
                return True

#simplify 3 var function
def three_var_sop(table, columns):
    sum_of_products = []
    for i in range(len(table)):
        if 0 not in table:
            sum_of_products.append('1')
            return sum_of_products
        if has_four_group(table, i):
            if i == 0 and table[i] == 1 and table[i+1] == 1 and table[i+3] ==1 and table[i+2] ==1:
                sum_of_products.append('A\'')
            elif i == 4 and table[i] == 1 and table[i+1] == 1 and table[i+3] ==1 and table[i+2] ==1:
                sum_of_products.append('A')
            elif columns[i][0] == columns[(i+1) % 4][0]:
                if columns[i][0] == '0':
                    sum_of_products.append('B\'')
                elif columns[i][0] == '1':
                    sum_of_products.append('B')
            elif columns[i][1] == columns[(i+1) % 4][1]:
                if columns[i][1] == '0':
                    sum_of_products.append('C\'')
                elif columns[i][1] == '1':
                    sum_of_products.append('C')
        if i >= 4 and i <= 7:   # row 2 A == 1
            if table[i] == 1 and table[((i + 1) % 4) + 4] == 1:
                if columns[i % 4][0] == columns[(i + 1) % 4][0]:
                    if columns[i % 4][0] == '1': #common B
                        sum_of_products.append('AB')
                    elif  columns[i % 4][0] == '0': #common B'
                        sum_of_products.append('AB\'')
                elif columns[i % 4][1] == columns[(i + 1) % 4][1]:
                    if columns[i % 4][1] == '1': #common C
                        sum_of_products.append('AC')
                    elif  columns[i % 4][1] == '0': #common C'
                        sum_of_products.append('AC\'')
            elif has_no_pair(table, i):
                if columns[i % 4] == '00':
                    sum_of_products.append('AB\'C\'')
                elif columns[i % 4] == '01':
                    sum_of_products.append('AB\'C')
                elif columns[i % 4] == '11':
                    sum_of_products.append('ABC')
                elif columns[i % 4] == '10':
                    sum_of_products.append('ABC\'')
        if i < 4:# check vertical pairs and first row A == 0
            if  table[i] == 1 and table[i + 4] == 1:
                sum_of_products.append(get_vert_pairs(table, columns, i))
            if table[i] == 1 and table[(i + 1) % 4] == 1:
                if columns[i % 4][0] == columns[(i + 1) % 4][0]:
                    if columns[i % 4][0] == '1': #common B
                        sum_of_products.append('A\'B')
                    elif  columns[i % 4][0] == '0': #common B'
                        sum_of_products.append('A\'B\'')
                elif columns[i % 4][1] == columns[(i + 1) % 4][1]:
                    if columns[i % 4][1] == '1': #common C
                        sum_of_products.append('A\'C')
                    elif  columns[i % 4][1] == '0': #common C'
                        sum_of_products.append('A\'C\'')
            elif has_no_pair(table, i):
                if columns[i] == '00':
                    sum_of_products.append('A\'B\'C\'')
                elif columns[i] == '01':
                    sum_of_products.append('A\'B\'C')
                elif columns[i] == '11':
                    sum_of_products.append('A\'BC')
                elif columns[i] == '10':
                    sum_of_products.append('A\'BC\'')
    return sum_of_products

# set up 3 var kmap
def three_variable_setup(kmap3):
    table,columns = BuildMap().three_var_map_format()
    sop = []
    for i in range(len(table)):
        for key in kmap3:
            if kmap3[key] == 1 and key == i:
                table[i] = kmap3[key]
    for i in range(len(table)):
        if i == 2 or i == 6:
            table[i],table[i+1] = table[i+1],table[i]
    sop = three_var_sop(table, columns)
    display_format(sop)

# simplify four var function
def four_var_sop(table, columns):
    sum_of_products = []
    for i in range(len(table)):
        if i < 4: # Row 1
            if table[i] == 1 and table[(i + 1) % 4] == 1:
                if columns[i][0] == '1' and columns[(i+1) % 4][0] == '1':# common C
                    sum_of_products.append('A\'B\'C')
                elif columns[i][0] == '0' and columns[(i+1) % 4][0] == '0':
                    sum_of_products.append('A\'B\'C\'')
                elif columns[i][1] == '1' and columns[(i+1) % 4][1] == '1':# common D
                    sum_of_products.append('A\'B\'D')
                elif columns[i][1] == '0' and columns[(i+1) % 4][1] == '0':
                    sum_of_products.append('A\'B\'D\'')
            if table[i] == 1 and table[i + 4] == 1:
                sum_of_products.append(get_vert_pairs(table, columns, i))
            elif has_no_pair(table, i):
                if columns[i] == '00':
                    sum_of_products.append('A\'B\'C\'D\'')
                elif columns[i] == '01':
                    sum_of_products.append('A\'B\'C\'D')
                elif columns[i] == '11':
                    sum_of_products.append('A\'B\'CD')
                elif columns[i] == '10':
                    sum_of_products.append('A\'B\'CD\'')
        elif i < 8 and i >= 4: # row 2
            if table[i] == 1 and table[((i + 1) % 4) + 4] == 1:
                if columns[i % 4][0] == '1' and columns[(i+1) % 4][0] == '1':
                    sum_of_products.append('A\'BC')
                elif columns[i % 4][0] == '0' and columns[(i+1) % 4][0] == '0':
                    sum_of_products.append('A\'BC\'')
                elif columns[i % 4][1] == '1' and columns[(i+1) % 4][1] == '1':
                    sum_of_products.append('A\'BD')
                elif columns[i % 4][1] == '0' and columns[(i+1) % 4][1] == '0':
                    sum_of_products.append('A\'BD\'')
            if table[i] == 1 and table[i + 4] == 1:
                sum_of_products.append(get_vert_pairs(table, columns, i))
            elif has_no_pair(table, i):
                if columns[i % 4] == '00':
                    sum_of_products.append('A\'BC\'D\'')
                elif columns[i % 4] == '01':
                    sum_of_products.append('A\'BC\'D')
                elif columns[i % 4] == '11':
                    sum_of_products.append('A\'BCD')
                elif columns[i % 4] == '10':
                    sum_of_products.append('A\'BCD\'')
        elif i >= 8 and i < 12: # row 3
            if table[i] == 1 and table[((i + 1) % 4) + 8] == 1:
                if columns[i % 4][0] == '1' and columns[(i+1) % 4][0] == '1':
                    sum_of_products.append('ABC')
                elif columns[i % 4][0] == '0' and columns[(i+1) % 4][0] == '0':
                    sum_of_products.append('ABC\'')
                elif columns[i % 4][1] == '1' and columns[(i+1) % 4][1] == '1':
                    sum_of_products.append('ABD')
                elif columns[i % 4][1] == '0' and columns[(i+1) % 4][1] == '0':
                    sum_of_products.append('ABD\'')
            if table[i] == 1 and table[i + 4] == 1:
                sum_of_products.append(get_vert_pairs(table, columns, i))
            elif has_no_pair(table, i):
                if columns[i % 4] == '00':
                    sum_of_products.append('ABC\'D\'')
                elif columns[i % 4] == '01':
                    sum_of_products.append('ABC\'D')
                elif columns[i % 4] == '11':
                    sum_of_products.append('ABCD')
                elif columns[i % 4] == '10':
                    sum_of_products.append('ABCD\'')
        elif i > 11 and i <= 15:
            if table[i] == 1 and table[((i + 1) % 4) + 12] == 1:
                if columns[i % 4][0] == '1' and columns[(i+1) % 4][0] == '1':
                    sum_of_products.append('AB\'C')
                elif columns[i % 4][0] == '0' and columns[(i+1) % 4][0] == '0':
                    sum_of_products.append('AB\'C\'')
                elif columns[i % 4][1] == '1' and columns[(i+1) % 4][1] == '1':
                    sum_of_products.append('AB\'D')
                elif columns[i % 4][1] == '0' and columns[(i+1) % 4][1] == '0':
                    sum_of_products.append('AB\'D\'')
            if table[i] == 1 and table[i % 4] == 1:
                sum_of_products.append(get_vert_pairs(table, columns, i))
            elif has_no_pair(table, i):
                if columns[i % 4] == '00':
                    sum_of_products.append('AB\'C\'D\'')
                elif columns[i % 4] == '01':
                    sum_of_products.append('AB\'C\'D')
                elif columns[i % 4] == '11':
                    sum_of_products.append('AB\'CD')
                elif columns[i % 4] == '10':
                    sum_of_products.append('AB\'CD\'')
    return sum_of_products

def four_variable_setup(kmap4):
    table, columns = BuildMap().four_var_map_format()
    sop = []
    for i in range(len(table)):
        for key in kmap4:
            if kmap4[key] == 1 and key == i:
                table[i] = kmap4[key]
    for i in range(len(table) // 2):
        if i == 2 or i == 6:
            table[i],table[i+1] = table[i+1],table[i]
    for i in range(8 , len(table)):
        if i == 10 or i == 14:
            table[i],table[i+1] = table[i+1],table[i]
    for i in range(8 , 12):
        table[i],table[i+4] = table[i+4], table[i]
    sop = four_var_sop(table, columns)
    display_format(sop)

def two_var_sop(table, columns):
    sum_of_products = []
    if has_four_group(table, 0):
        sum_of_products.append('1')
        return sum_of_products
    else:
        for i in range(len(table)):
            if i == 0:   # row 1 A==0
                if table[i] == table[(i+1)] and table[i] == 1:  # horizontal pair
                    sum_of_products.append('A\'')
                if has_no_pair(table, i):
                    sum_of_products.append('A\'B\'')
                if table[i] == 1 and table[i+2] == 1:
                    sum_of_products.append(get_vert_pairs(table, columns, i))
            if i == 1:
                if table[i] == 1 and table[i+2] == 1:
                    sum_of_products.append(get_vert_pairs(table, columns, i))
                if has_no_pair(table, i):
                    sum_of_products.append('A\'B')
            if i == 2:   # row 2 A==1
                if table[i] == table[i+1] and table[i] == 1:    #horizontal pair
                    sum_of_products.append('A')
                if has_no_pair(table, i):
                    sum_of_products.append('AB\'')
            if i == 3:
                if has_no_pair(table, i):
                    sum_of_products.append('AB')

        return sum_of_products

def two_variable_setup(kmap2):
    table, columns = BuildMap().two_var_map_format()
    for key in kmap2:
        for i in range(len(table)):
            if kmap2[key] == 1 and key == i:
                table[i] = kmap2[key]
    sop = two_var_sop(table, columns)
    display_format(sop)

def main():
    minterms = []
    kmap_vars = 0
    minterms, kmap_vars = get_input()
    kmap2 = BuildMap().two_var_kmap()
    kmap3 = BuildMap().three_var_kmap()
    kmap4 = BuildMap().four_var_kmap()
    print("Number of variables: ", kmap_vars)
    print("Minterm values: ", ', '.join(map(str, minterms)))
    
    if kmap_vars == 2:
        for num in minterms:
            for key in kmap2:
                if num == key:
                    kmap2[key] = 1
        two_variable_setup(kmap2)
    elif kmap_vars == 3:
        for num in minterms:
            for key in kmap3:
                if num == key:
                    kmap3[key] = 1
        three_variable_setup(kmap3)
    elif kmap_vars == 4:
        for num in minterms:
            for key in kmap4:
                if num == key:
                    kmap4[key] = 1
        four_variable_setup(kmap4)


if __name__ == "__main__":
    main()
