import torch

x = torch.tensor([1,2,3,4,5])
y = torch.tensor([10,20,30,40,50])

condition = x>3
# 第一个张量符合condition的情况下会被留下来，否则就会被第二个张量的值替换
result = torch.where(condition, x, y)
print(result) # output tensor([10, 20, 30,  4,  5])

t = torch.arange(0, 10, 2)
print(t)# output tensor([0, 2, 4, 6, 8])

t2 = torch.arange(5,0,-1)
print(t2)# output tensor([5, 4, 3, 2, 1])