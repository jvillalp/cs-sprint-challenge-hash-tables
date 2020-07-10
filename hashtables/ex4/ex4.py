## Understand
    # create dic of positive num's where there is a negavtive number behind it. 
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    #create dic.
    corr_num = {}
    #if a pos num has a neg num, add to result []
    result = []
    #find num inside of list (range of length of array)- range(len(a))
    for num in range(len(a)):
        #if value of num in list in dic negative
        if -a[num] in corr_num:
            #if value of num we are iterating thorugh is positive
            if a[num] > 0:
                #result.append num( the postive value) to result's list
                result.append(a[num])
            else:
                #result.append neg value to list
                result.append(-a[num])
        #want to create temp key = True, to be able to compare value to list to find corresponding value
        corr_num[a[num]] = True
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
