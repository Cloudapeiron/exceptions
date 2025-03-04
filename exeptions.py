class JustNotCoolError(Exception):
  pass

x = 2
try:
  raise JustNotCoolError('This is not cool.')
  # raise Exception("I'm a custom exception!")
  # print(x / 1)
  # if not type(x) is str:
  # raise TypeError("Only strings are allowed")
except NameError:
  print('NameError means something is undefined')
except ZeroDivisionError:
  print('ZeroDivisionError means you tried to divide by zero')
except Exception as error:
  print(error)
else:
  print('No errors occurred')
finally:
  print('This will always run') 