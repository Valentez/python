my_rating_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]
copy_rating = my_rating_list.copy()
nrating = int(input("Please, input new rating element: "))
if nrating >= my_rating_list[-1]:
    my_rating_list.append(nrating)
    print(f"Input number {nrating} inserted to end of list: {my_rating_list}")
else:
    i = 0
    while i < len(my_rating_list):
        if nrating < my_rating_list[i]:
            my_rating_list.insert(i, nrating)
            print(f"Input number has position {i} in {my_rating_list}")
        elif nrating == my_rating_list[i]:
            my_rating_list.insert(i+1, nrating)
            print(f"Input number has position {i+1} in {my_rating_list}")
            break
        i += 1
