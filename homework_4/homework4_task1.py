from sys import argv


def calc_zp():
    return float(argv[1]) * float(argv[2]) + float(argv[3])


print("ZP=%.2f" %(calc_zp()))
