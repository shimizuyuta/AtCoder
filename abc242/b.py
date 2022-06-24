from numpy import sort


def main():
  word = list(input())
  sorted_word = sorted(word)
  print("".join(sorted_word))

if __name__ == "__main__":
  main()