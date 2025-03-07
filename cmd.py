import argparse

def calculate_rectangle_area(length, width):
   return length * width

def main():

   # Create an ArgumentParser object with a description
   parser = argparse.ArgumentParser(description='Calculate the area of a rectangle.')

   # Define command-line arguments
   parser.add_argument('length', type=int, help='Length of the rectangle')
   parser.add_argument('width', type=int, help='Width of the rectangle')

   # Parse the command-line arguments
   args = parser.parse_args()

   # Calculate the area
   area = calculate_rectangle_area(args.length, args.width)

   # Display the result
   print(f'The area of the rectangle with length {args.length} and width {args.width} is {area:.2f}')

if __name__ == "__main__":

   main()



   