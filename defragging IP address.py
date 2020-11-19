def main():
    address = "1.1.1.1"
    list2 = []
    new_list = address.split(".")
    for i in new_list:
        list2.append(i)
        list2.append("[.]")
    list2 = list2[:-1]
    for t in list2:
        print(t, end='')

main()
