TODO: Reflect on what you learned this week and what is still unclear.
Commit and push after each weeks exercises to submit
learning how to use if and else 
used elif in exercise 3. read as else if
create a list: list = []
for x in range(enter the number of list you want).... use this to determine how many lists you want

list = []                       define a list

    for x in range(10):         determine how many lists you want
        list1 = []              define list1 which determines what is with in the 10 lists
        for y in range(5):              how many expressions within each list 
            list1.append("(" + "i" + str(x) + "," + " " + "j" + str(y) + ")")           

            .append decides what the expressions are
            str(x) = 0 to 9,  str(y) = 0 to 5

        list.append(list1)          means the list1 is what fills in the 10 lists
    return list