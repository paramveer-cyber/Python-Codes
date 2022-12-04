arr = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
new_arr = []

def reverse_arr(arr, new_arr):
    for i in range((arr.__len__())):
        new_arr.append(arr[arr.__len__()-(i+1)])
    return new_arr

print(f"Rainbow Colours: {reverse_arr(arr, new_arr)}")