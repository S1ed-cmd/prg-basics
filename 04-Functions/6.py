def f(credit_number):
    enter = credit_number[:4] + "*"*10 + credit_number[-2:]
    return enter



if __name__ == "__main__":
  print(f("5290312400019022"))

