
# 아래에 코드를 작성하시오.
movies = [['Inception', 9], ['Interstellar', 8.5], ['Dunkirk', 7.5], ['Tenet', 6]]

new_movies = []
for movie in movies:
    temp_dict = {}
    temp_dict['title'] = movie[0]
    temp_dict['rating'] = movie[1]
    new_movies.append(temp_dict)

def get_high_rated_movies(threshold):
    result = f'Movies with a rating of {threshold:.1f} or higher\n'
    for movie in new_movies:
        if movie.get('rating') >= threshold:
            result = result + movie.get('title') + '\n'
    return result

threshold = int(input("Enter the rating threshold:"))
print(get_high_rated_movies(threshold))