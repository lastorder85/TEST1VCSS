import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    assert(sum(alist)<100),"sum >100"
    assert(len(alist)!=0),"sum is null"
    return alist

def printIT():
    print(generate_list())
    
def main():
    printIT()

if __name__ =='__main__':
    print("Test printIT():")
    main()