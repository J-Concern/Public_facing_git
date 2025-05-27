import random
import math

def is_sorted(array, ascending = True):
    #helper function, can measure if an array is sorted in O(n) worst case.
    for i in range(0,int(len(array)-1)):
        #iterates through the array
        if ascending == True:
            #for ascending cases compares index with its right neighbor
            if array[i] > array[i+1]:
                return False
        if ascending == False:
            #for desceding cases compares index with left neighbor
            if array[i] < array[i+1]:
                return False
    #if iterates through with no False returns then returns true. 
    return True

def number_sort_algo(array, ascending = True):
    # this is not quick sort unfortunately.
    # this does the work of sorting in best case O n log(n) time. 
    if len(array) <= 2:
        #removes edge cases of array being to small, if True returns array.
        print("Array too Short.")
        return array
    
    # initates a step counter to measure efficiency.
    step_counter = 0

    while is_sorted(array) == False:
        # this while loop runs until is_sorted returns true.
    
        #increments the step counter by 1
        step_counter += 1

        #determines a random pivot and gets the index.
        pivot_index = math.floor(random.randint(0, (len(array)-1)))
        pivot = array[pivot_index]
        
        #creates arrays to store the wings of data.
        less_than = []
        greater_than = []

        if ascending == True:
            #for ascending iterates through and appends greater and less than.
            for i in array:
                if i <= pivot:
                    less_than.append(i)
                else:
                    greater_than.append(i)

        if ascending == False:
            #for ascending iterates through and appends greater and less than.
            for i in array:
                if i >= pivot:
                    less_than.append(i)
                else:
                    greater_than.append(i)
        array = less_than + greater_than

    if is_sorted(array) == True:
        #checks if array is sorted, if True returns array.
        return array, step_counter
    
    else:
        #error control, if something fails this should be able to pass False
        print("Error")
        return False

def sort_algo_test(array_size):
    #a small test function
    custom_algo = []
    quick_sort_algo = []
    for i in range(number_of_tests):
        array = [random.randint(1,1000) for i in range(array_size)]
        array2 = array.copy()
        array2, step_counter = number_sort_algo(array)
        custom_algo.append(step_counter)
        #print(f"Total Number of Steps: {step_counter}.")
        #print(array2)
        array, stepcounter = quick_sort(array,True, True)
        #print(f"Total Number of Steps: {stepcounter}.")
        quick_sort_algo.append(stepcounter)
        #print(array)
    print(f"Average steps for Custom Algo:{sum(custom_algo)/len(custom_algo)}.")
    print(f"Best case for Custom Algo: {min(custom_algo)}.")
    print(f"Average steps for Quick Sort:{sum(quick_sort_algo)/len(quick_sort_algo)}.")
    print(f"Best case for Quick Sort: {min(quick_sort_algo)}.")

sort_algo_test(10,5000)