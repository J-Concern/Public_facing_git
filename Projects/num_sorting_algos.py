import random
import math


#SORT CHECKER
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



#CUSTOM SORT
def number_sort_algo(array, ascending = True):
    # this does the work of sorting in best case On, worst case O (n!)
    if len(array) <= 1:
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



#QUICKSORT
def quick_sort(array, ascending = True, first_step = True, stepcounter = 0):
    # best case o(nlogn) worst case o(n^2)
    if first_step == True:
        # sets the step counter, to help with tracking
        first_step = False

    if len(array) <= 1:
        #removes edge cases of array being to small, if True returns array.
        return array, stepcounter

    stepcounter = stepcounter + 1

    #determines a random pivot and gets the index.
    pivot_index = math.floor(random.randint(0, (len(array)-1)))
    pivot = array[pivot_index]

    
    #creates arrays to store the wings of data.
    less_than = []
    greater_than = []

    for i in array[:pivot_index] + array[pivot_index + 1:]:

        if ascending == True:
            if i <= pivot:
                less_than.append(i)
            else:
                greater_than.append(i)

        if ascending == False:
            if i >= pivot:
                less_than.append(i)
            else:
                greater_than.append(i)

    #recursively sorts left and right in infinte fashion.
    sorted_left, stepcounter = quick_sort(less_than, ascending, False, stepcounter)
    sorted_right, stepcounter = quick_sort(greater_than, ascending, False, stepcounter)

    return sorted_left + [pivot] + sorted_right, stepcounter



#MERGE SORT
def merge_sort(array, first_step = True, stepcounter = 0):
    if first_step == True:
        # sets the step counter, to help with tracking
        first_step = False

    if len(array) <= 1:
        #removes edge cases of array being to small, if True returns array.
        return array, stepcounter

    stepcounter = stepcounter + 1
    midpoint = len(array)//2
    #split into individual units
    left = array[:midpoint]
    right = array[midpoint:]
    #recursive calls
    sorted_left, stepcounter = merge_sort(left, False, stepcounter)
    sorted_right, stepcounter= merge_sort(right, False, stepcounter)
    #returns with merge helper function
    return merge(sorted_left, sorted_right), stepcounter

def merge(left,right):
    #merge helper function
    result = []
    position_left = position_right = 0
    #opens while loop to interate through positions
    while position_left < len(left) and position_right < len(right):
        #left side
        if left[position_left] < right[position_right]:
            result.append(left[position_left])
            position_left +=1
        #right side
        else:
            result.append(right[position_right])
            position_right +=1
        #could program a block for reversal of ascending vs decending here
        #would probably end up with a deeper level of abstraction
    result.extend(left[position_left:])
    result.extend(right[position_right:])

    return result

# random single dimensional array generator.
def random_1d_array_gen(max_int, array_size):
    array = [random.randint(1, max_int, ) for i in range(array_size)]
    return array


#Sort Comparator
def sort_algo_test(array_size, number_of_tests):
    #a small test function
    custom_algo = []
    quick_sort_algo = []
    merge_sort_algo = []
    for i in range(number_of_tests):
        array = [random.randint(1,1000) for i in range(array_size)]
        array2 = array.copy()
        array3 = array.copy()
        array2, step_counter = number_sort_algo(array)
        custom_algo.append(step_counter)
        array, stepcounter = quick_sort(array,True)
        quick_sort_algo.append(stepcounter)
        array3, stepcounter = merge_sort(array,True)
        merge_sort_algo.append(stepcounter)
    print(f"Average steps for Custom Algo:{sum(custom_algo)/len(custom_algo)}.")
    print(f"Best case for Custom Algo: {min(custom_algo)}.\n")
    print(f"Average steps for Quick Sort:{sum(quick_sort_algo)/len(quick_sort_algo)}.")
    print(f"Best case for Quick Sort: {min(quick_sort_algo)}.\n")
    print(f"Average steps for Merge Sort:{sum(merge_sort_algo)/len(merge_sort_algo)}.")
    print(f"Best case for Merge Sort: {min(merge_sort_algo)}.")

if __name__ == "__main__":
    sort_algo_test(1000,5)