# python3
#Evelīna Paula Ķerķe 221RDB044

def build_heap(data):
    swaps = []
    # TODO: Create heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)
    swapCount = 0 
    for i in range(n//2, -1, -1): 
        right = 2 * i + 2
        left = 2 * i + 1
        small = i 
        if right < n and data[right] < data[small]: 
            small = right
        if left < n and data[left] < data[small]: 
            small = left
        if small != i:
            data[i], data[small] = data[small], data[i] 
            swaps.append((i,small))
            swapCount += 1 
            j = small 
            while j < n//2:  
                right = 2 * j + 2
                left = 2 * j + 1 
                small = j 
                if right < n and data[right] < data[small]: 
                    small = right
                if left < n and data[left] < data[small]: 
                    small = left
                if small != j: 
                    data[j], data[small] = data[small], data[j] 
                    swaps.append((j,small))
                    swapCount += 1 
                    j = small 
                else: 
                    break
    return swaps, swapCount


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    text = input() 
    if "F" in text: 
        fileName = input()  
        if "a" in fileName: 
            return 
        with open(fileName, mode="r") as file: 
            n = int(file.readline().strip()) 
            data = list(map(int, file.readline().split())) 
    if "I" in text: 
        n = int(input()) 
        data = list(map(int, input().split())) 

    # input from keyboard

    # calls function to assess the data 
    # and give back all swaps
    swaps, swapCount = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(swapCount)
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
