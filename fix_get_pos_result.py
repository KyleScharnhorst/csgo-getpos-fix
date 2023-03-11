import sys
import os

z_magic_value = float("64.062561")
setpos_z_val_index = 4

def print_help():
    print('call like this:')
    print('python', os.path.basename(__file__), '"setpos -800.009644 -2879.966309 239.025986;setang -23.661070 114.181854 0.000000"')
    print('Need quotes.')

def handle_single_arg():
    getpos_output = sys.argv[1]
    setpos_and_setang = getpos_output.split(";")
    split_setpos = setpos_and_setang[0].split(" ")
    z_value = float(split_setpos[3])
    # print(z_value)
    # print(z_value - z_magic_value)
    modified_z_value =  z_value - z_magic_value
    modified_z_value = round(modified_z_value, 6)
    # print(round(modified_z_value, 6))
    split_setpos[3] = str(modified_z_value)
    new_setpos_str = ' '.join(split_setpos)
    setpos_and_setang[0] = new_setpos_str
    result = ';'.join(setpos_and_setang)
    print(result)

if __name__ == "__main__":
    try:
        arg_count = len(sys.argv)
        # print('arg_count: ', arg_count)
        # print(sys.argv[0])
        # print(sys.argv[1])
        # print('magic: ', z_magic_value)

        # first arg is filename
        if arg_count == 2:
            handle_single_arg()
        else:
            raise Exception("Must provide a single argument.")
    except Exception as e:
        print(e)
        print_help()
