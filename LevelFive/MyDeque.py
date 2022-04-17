import string
import collections


# print(string.ascii_lowercase)

def main():
    myd = collections.deque(string.ascii_lowercase)
    print("Number of elements are:", str(len(myd)))
    # print(myd)
    # for i in myd:
    #     print(i, end=',')
    myd.appendleft(111111)
    myd.pop()
    print(myd)


if __name__ == '__main__':
    main()
