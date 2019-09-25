x = 10
func_a = lambda y: x + y

x = 20
func_b = lambda y: x + y

print(func_a(10))
print(func_b(10))
x = 30

print(func_a(10))
print(func_b(10))

func_list_a = [lambda z: z + n for n in range(5)]
for func_in_list_a in func_list_a:
    print(func_in_list_a(10))

func_list_a = [lambda z, n=n: z + n for n in range(5)]
for func_in_list_a in func_list_a:
    print(func_in_list_a(10))
