movies = 0
List = []
while movies != "quit" and len(List) != 5:
    movies = input("Enter a movie").lower()
    List.append(movies)
print(List[:len(List)-1])
