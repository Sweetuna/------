for i in range(2,10) : 
    print(f"# {i}단 #      ", end="\t")
print()

for k in range(1, 10) :
    for i in range(2, 10) :
        print(f"{i} x {k} = {i*k}", end="\t")
    print()