python_batch = {'Dhruv','Arman','Dhwani','Arjun'}
ds_datch = {'Dhruv','Dhwani','Parth','Radhika'}

print("Both",python_batch & ds_datch)
print("any",python_batch | ds_datch)
print("only ds batch =", ds_datch - python_batch)