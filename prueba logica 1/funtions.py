#Fizz buzz
def fizz_buzz_numbers():
  fizz_buzz_numbers=[]
  for i in range(101):
    if  i%3==0 and i%5==0:
      fizz_buzz_numbers.append("fizz buzz")
    elif i%3 == 0:
      fizz_buzz_numbers.append("fizz")
    elif i%5 == 0:
      fizz_buzz_numbers.append("buzz")
    else:
      fizz_buzz_numbers.append(i)
  return fizz_buzz_numbers

#Fibonacci
def fibonacci_funtion(n):
    
    n1, n2 = 0, 1
    count = 0

    if n == 1 or n == 0:
       return n
    else:
        while count < n:
          nth = n1 + n2
          n1 = n2
          n2 = nth
          count += 1
        return n1
    
#Words counter

def text_contained(text:str):
  
  signals=["?","!",",",".",""]
  for signal in signals:
    text=text.replace(signal,"")
  text_list=text.lower().split(" ")

  count=[text_list.count(word) for word in text_list]
  counted={text_list[i]:count[i] for i in range(len(text_list))}
  return counted