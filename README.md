# Conditionals with Lists

## Problem Checklist

  * [ ] add
  * [ ] multiplier
  * [ ] greater_than
  * [ ] in_out
  * [ ] consecutives



## Notes

### Looping using the index (position)

If we need to know the position of an item in the list, we can
iterate through the index of each item:

``` python

nums = [1, 2, 3, 4, 5]

length = len(nums)
for i in range(length):
	n = nums[i]
	print(n)

```

### Looping through the values

In most cases, we want to just know the value of each item
in the list and do something with it. This is simpler, and
should be used in most cases:

``` python

nums = [1, 2, 3, 4, 5]

for n in nums:
	print(n)
```


### Advanced - Using Enumerate

Python has a special enumerate function that we can use
to iterate through both index and value:

``` python

nums = [1, 2, 3, 4, 5]

for i, n in enumerate(nums):
	print("In position:", i, "is", n)
```

This works just like iterating through the index and assigning
`nums[i]` to `n` each loop. It can make the code look cleaner
though.
