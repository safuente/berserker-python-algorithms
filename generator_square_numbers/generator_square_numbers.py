def generate_square(nums):
    for num in nums:
        yield num ** 2


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = list(generate_square(nums))
print(square_list)