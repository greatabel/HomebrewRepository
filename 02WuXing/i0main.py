import i1config as config


def main():
    # 无须担心顺序，py3.6之后dict顺序固化了
    d = list(config.WuXing.items())

    for i in range(len(d)):
        if i != len(d)-1:
            print(d[i], '->生->', d[i+1])
        else:
            print(d[i], '->生->', d[0])


if __name__ == '__main__':
    main()
