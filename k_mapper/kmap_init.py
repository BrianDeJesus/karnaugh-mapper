
class BuildMap:
    #format initializations
    def __init__(self):
        self.columns = []
        self.map_table = []
    def three_var_map_format(self):
        self.columns = ['00', '01', '11', '10']
        self.map_table = [0] * 8
        return self.map_table, self.columns
    def four_var_map_format(self):
        self.columns = ['00', '01', '11', '10']
        self.map_table = [0] * 16
        return self.map_table, self.columns
    def two_var_map_format(self):
        self.columns = [0, 1]
        self.map_table = [0] * 4
        return self.map_table, self.columns
    #actual kmap initializations
    def two_var_kmap(self):
        self.kmap2 = {0: 0, 1: 0, 2: 0, 3: 0}
        return self.kmap2
    def three_var_kmap(self):
        self.kmap3 = {0: 0, 1: 0, 3: 0, 2: 0, 4: 0, 5: 0, 7: 0, 6: 0}
        return self.kmap3
    def four_var_kmap(self):
        self.kmap4 = {0: 0, 1: 0, 3: 0, 2: 0, 4: 0, 5: 0, 7: 0, 6: 0, 12: 0, 13: 0, 15: 0, 14: 0, 8: 0, 9: 0, 11: 0, 10: 0}
        return self.kmap4
