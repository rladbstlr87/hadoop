
import sys

current_movie_id = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    movie_id, rating = line.split()

    try:
        rating = float(rating)
    except:
        continue
    
    if current_movie_id == movie_id:
        current_count += 1
        current_sum += rating
    else:
        if current_movie_id is not None:
            current_avg = current_sum / current_count
            print(f'{current_movie_id}\t{current_avg}')

        current_movie_id = movie_id
        current_count = 1
        current_sum = rating

current_avg = current_sum / current_count
print(f'{current_movie_id}\t{current_avg}')