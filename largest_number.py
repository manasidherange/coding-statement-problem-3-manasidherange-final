#MANASI DHERANGE
#PROBLEM STATEMENT 3
def largest_number(nums):
  #converts all no. to str for comparison
  nums_str = [str(num) for num in nums]

  #by bubble sort for simplicity and clarity
  for i in range(len(nums_str)):
    for j in range(i+1, len(nums_str)):
      #compare concatenated str
      if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
        #swap if needed
        nums_str[i] , nums_str[j] = nums_str[j], nums_str[i]

  #join all str
  result = ''.join(nums_str)

  #handle edge case wwhere all numbers are zero
  if result[0] == '0':
    return "0"

  return result

def main():
  #i/p from user
  try:
    input_str = input("Enter numbers separated by spaces:")
    #convert str to int
    nums = [int(x) for x in input_str.split()]
    result = largest_number(nums)
    
    #dsiplay results
    print(f"Input: {nums}")
    print(f"Largest concatenated number:{result}")

  except ValueError:
    print("Error :Please enter valid int only!")
  except Exception as e:
    print(f"An error occured:{e}")

if __name__ =="__main__":
  main()
    
