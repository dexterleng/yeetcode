def two_sum(numbers, target):
    lookup = {}
    for i in range(len(numbers)):
      n = numbers[i]
      if (target - n) in lookup:
        return [lookup[target - n], i]
      lookup[n] = i
    return -1
