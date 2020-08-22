# Link - https://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/

# A O(n) Python 3 program to find
# maximum product pair in an array

# Function to find maximum product
# pair in arr[0..n-1]
def maxProduct(arr, n):
    if (n < 2):
        print("No pairs exists")
        return

    if (n == 2):
        print(arr[0], " ", arr[1])
        return

    # Iniitialize maximum and
    # second maximum
    posa = 0
    posb = 0

    # Iniitialize minimum and
    # second minimum
    nega = 0
    negb = 0

    # Traverse given array
    for i in range(n):

        # Update maximum and second
        # maximum if needed
        if (arr[i] > posa):
            posb = posa
            posa = arr[i]

        elif (arr[i] > posb):
            posb = arr[i]

        # Update minimum and second
        # minimum if needed
        if (arr[i] < 0 and abs(arr[i]) > abs(nega)):
            negb = nega
            nega = arr[i]

        elif (arr[i] < 0 and abs(arr[i]) > abs(negb)):
            negb = arr[i]

    if (nega * negb > posa * posb):
        print("Max product pair is {",
              nega, ", ", negb, "}")
    else:
        print("Max product pair is {",
              posa, ", ", posb, "}")

    # Driver Code


if __name__ == "__main__":
    arr = [1, 4, 3, 6, 7, 0]
    n = len(arr)
    maxProduct(arr, n)

# This code is contributed
# by ChitraNayal
