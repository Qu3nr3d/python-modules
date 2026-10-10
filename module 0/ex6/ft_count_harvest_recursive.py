def ft_count_harvest_recursive(days=0, i=1):
    if days == 0:
        days = int(input("Days until harvest:"))
    if i <= days:
        print(f"Day {i}")
        ft_count_harvest_recursive(days, i+1)
    else:
        print("Harvest time!")


ft_count_harvest_recursive()
