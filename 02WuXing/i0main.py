import i1config as config


def main():
    # 无须担心顺序，py3.6之后dict顺序固化了
    d = list(config.WuXing.items())

    for i in range(len(d)):
        print(d[i], '->生->', d[(i+1)%len(d)])


    for i in range(len(d)):
        print(d[i], '->克->', d[(i+2)%len(d)])

if __name__ == '__main__':
    main()
