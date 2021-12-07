names = ['vasia', 'kate','peti','egorr']
def get_names(names):
    return [k for k in names if len(k) == 4]

print (get_names(names))