flatten_matrix = []

sub_mats = [mtx.strip() for mtx in input().split('|')]

for mtx in sub_mats[::-1]:
    nums = mtx.split()
    flatten_matrix.extend(nums)

print(' '.join(flatten_matrix))