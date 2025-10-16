marks=[85,90,78,65,78,44,34]
search_item=78
found=False
for i in range(len(marks)):
    if marks[i]==search_item:
        print("Item found at index",i)
        found=True
        break
    if not found:
        print("Item not found")
