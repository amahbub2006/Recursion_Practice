def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def even_and_odd_count(value):
    even_count = 0
    odd_count = 0
    while value > 0:
        last_digit = value % 10
        if last_digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        value //= 10
    return even_count, odd_count

def reverse_display(s):
    if len(s) == 0:
        return ''
    else:
        return reverse_display(s[1:]) + s[0]

def count_occurrences(s, a):
    if len(s) == 0:
        return 0
    if s[-1] == a:
        return 1 + count_occurrences(s[:-1], a)
    else:
        return count_occurrences(s[:-1], a)

def product_digits(n):
    if n < 10:
        return n
    else:
        return (n % 10) * product_digits(n // 10)

def reverse_display_with_index(s, high):
    if high < 0:
        return ''
    else:
        return s[high] + reverse_display_with_index(s, high - 1)

def find_smallest(arr, size):
    if size == 1:
        return arr[0]
    else:
        return min(arr[size - 1], find_smallest(arr, size - 1))

def sum_array(arr, size):
    if size <= 0:
        return 0
    return sum_array(arr, size - 1) + arr[size - 1]

def main():
    while True:
        print("1. GCD")
        print("2. Even and Odd Count")
        print("3. Reverse Display")
        print("4. Count Occurrences of a Character")
        print("5. Product of Digits")
        print("6. String Reverse Display with Index")
        print("7. Find the Smallest Element in Array")
        print("8. Sum of Elements in Array")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num1 = int(input("Enter first integer: "))
            num2 = int(input("Enter second integer: "))
            print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")

        elif choice == 2:
            num = int(input("Enter an integer: "))
            even_count, odd_count = even_and_odd_count(num)
            print(f"Number of even digits: {even_count}")
            print(f"Number of odd digits: {odd_count}")

        elif choice == 3:
            s = input("Enter a string: ")
            print("Reversed string:", reverse_display(s))

        elif choice == 4:
            s = input("Enter a string: ")
            a = input("Enter a character: ")
            print(f"Occurrences of '{a}': {count_occurrences(s, a)}")

        elif choice == 5:
            num = int(input("Enter an integer: "))
            print(f"Product of digits: {product_digits(num)}")

        elif choice == 6:
            s = input("Enter a string: ")
            print("Reversed string:", reverse_display_with_index(s, len(s) - 1))

        elif choice == 7:
            arr = [int(x) for x in input("Enter integers separated by space: ").split()]
            print(f"Smallest element: {find_smallest(arr, len(arr))}")

        elif choice == 8:
            arr = [int(x) for x in input("Enter integers separated by space: ").split()]
            print(f"Sum of elements: {sum_array(arr, len(arr))}")

        elif choice == 9:
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
