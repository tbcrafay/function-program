'''Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''

def make_shirt(size, message):
  """
  Summarizes the size and message printed on a custom t-shirt.

  Args:
    size: The size of the shirt (e.g., "L").
    message: The message to be printed on the shirt.

  Returns:
    None
  """
  print(f"I'm making a {size} shirt with the message '{message}' printed on it.")

# Call the function with positional arguments
make_shirt("M", "I love Python!")

# Call the function with keyword arguments
make_shirt(message="Learning is fun!", size="XL")


