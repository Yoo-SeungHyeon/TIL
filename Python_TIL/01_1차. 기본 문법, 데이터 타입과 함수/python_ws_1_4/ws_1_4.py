# 아래에 코드를 작성하시오.

movies = []
movies.extend(['Inception','Interstellar','Dunkirk','Tebet'])

def get_movie_recommendation(input):
    if input >= 9:
        return 'Inception'
    elif input >= 8:
        return "Interstellar"
    elif input >= 7:
        return "Dunkirk"
    else: return "Tenet"
rating = int(input("Enter your movie rating (0-10):"))
print("Recommended movie:",get_movie_recommendation(rating))