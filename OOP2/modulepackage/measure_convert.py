
def inch_to_cm(inch:float):
    return f'{inch * 2.54:,.2f}'

def cm_to_inch(cm:float):
    return f'{cm / 2.54:,.2f}'

if __name__ == '__main__':
    print(inch_to_cm(2.54))
    print(cm_to_inch(5))