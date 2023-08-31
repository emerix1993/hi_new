# def search_word(word):
#     while True:
#     a = []
#     with open("rockyou1.txt", "r") as rockyou:
#         content = rockyou.read()
#         word = input("Enter a word: ")
#         if word in content:
#             a.append(word)
#         else:
#             print("This word not in file")
#     yield a
import os

from pympler.asizeof import asizeof


def search_word():
    with open("rockyou1.txt", "r") as rockyou:
        while True:
            word = input("Enter a word: ")
            found = False
            line = rockyou.readline()
            while line:
                if word in line:
                    found = True
                    yield line.rstrip()
                line = rockyou.readline()
            if not found:
                print("This word not in file")
            rockyou.seek(0)
            command1 = input("Do you want to stop process:(yes or no): ").strip().lower()
            if command1 == "yes":
                raise SystemExit("Process stopped by user")
            elif command1 == "no":
                pass


while True:
    with open("results.txt", "a") as result1:
        count = 0
        for result in search_word():
            print(result)
            result1.write(result + "\n")
            count += 1
            print(f"Total lines {count}")
            pympler_size = asizeof(result)
            os_size = os.path.getsize('results.txt')
            print(f"Pympler size: {pympler_size} bytes")
            print(f"All size: {os_size} bytes")
