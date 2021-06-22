# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

Input_list  = [1,2,3,5]
Input_list2  = [-1,1,2,3,5]
def sorterd_list_to_sqr(sort_list:list):
    finis = []

    for i in sort_list:
        finis.append()

    sort_list= sorted(sort_list)
    for i in sort_list:

        finis.append(abs(i)*i)

    return finis


Input_list3  = [-1,1,2,3,5, 1.0, '1',0 , '0xff']
data_set = [0, -1 ,1, 100000000000000000000000000000]

print(sorterd_list_to_sqr(Input_list3))



