from funtions import fibonacci_funtion,fizz_buzz_numbers, text_contained

def main():

    print(fibonacci_funtion(int(input("Input a number: "))))
    
    print(f"fizz_buzz_numbers{fizz_buzz_numbers()}")

    print(text_contained(str(input("Input a text: "))))

main()
