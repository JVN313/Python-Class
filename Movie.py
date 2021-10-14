current_movies = {"New Man":"12:00",
                  "Hello":"8:00"}

print("Show List")
for key in current_movies:
    print(key)
movie = input("pick one: ")
show=current_movies.get(movie)
print(show)