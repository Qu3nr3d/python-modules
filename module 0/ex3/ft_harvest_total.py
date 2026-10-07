def ft_harvest_total():
    harvests = [0,0,0]
    total_harvest = 0
    i = 0
    while i < 3:
        harvests[i] = int(input(f"Day {i + 1} harvest: "))
        total_harvest += harvests[i]
        i += 1
    print(f"Total Harvest: {total_harvest}")