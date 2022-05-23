import os


def main():
    i = 0
    path = input('Input Directory link: ')
    base_name = input('Enter base filename: ')
    ftype = input('Enter file extension ex:"exe", "py" etc.')
    path = ''.join([k if k != '\\' else '/' for k in path])
    path += '/'

    for filename in os.listdir(path):
        f = base_name + str(i) + '.' + ftype
        s = path + filename
        d = path + f

        os.rename(s, d)
        i += 1


if __name__ == '__main__':
    main()
