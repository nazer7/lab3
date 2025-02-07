def histogram(lst):
    for num in lst:
        print('*' * num)  
numbers = list(map(int, input("enters nums: ").split()))
histogram(numbers)
