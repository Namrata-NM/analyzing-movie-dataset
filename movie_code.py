from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """

    data_=dataset[start:end]
    for i in data_:
        print(i)
        print('\n')
    if rows_and_columns=='True':
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
     


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    """
    unique=[]
    duplicate=[]
    for rows in dataset:
        movie_name=rows[index_]
        if movie_name in unique:
            duplicate.append(movie_name)
        else : 
            unique.append(movie_name)
    print('Number of Duplicate Enteries are',len(duplicate))
    print('Some examples of Duplicate entries:\n',duplicate[:5])

def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_=[]
    for i in dataset:
        language=i[index_]
        if language==lang_:
            movies_.append(i)
    print("Movies in English Language:\n")    
    explore_data(movies_, 0, 3, True)
    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you have extracted the movies, call the explore_data() to print first few rows.
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies=[]
    for i in dataset:
        rating=float(i[-4])
        if ((rating>=rate_low) & (rating<=rate_high)):
            rated_movies.append(i)
    
    print('Examples of Movies in rate bucket')
    explore_data(rated_movies,0,3,True)
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)



# The first row is header. Extract and store it in 'movies_header'.

movies_header = movies[0]
print('Movie Information includes\n')
print(movies_header)
# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies=movies[1:]
#print(movies)


# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
print("Details of row 4553:")
explore_data(movies, 4553, 4554)

del movies[4553]


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
print('First five rows')
explore_data(movies,0,5,rows_and_columns='True')

# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.

duplicate_and_unique_movies(movies,13)

# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
review_max={}
for i in movies:
    movie_name=i[13]
    max_reviews=float(i[-3])
    if movie_name in review_max and review_max[movie_name] < max_reviews:
        review_max[movie_name]=max_reviews
    if movie_name not in review_max:
        review_max[movie_name]=max_reviews
    

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = []
repeated_movies = []

for i in movies:
    movie_name = i[13]
    max_reviews = float(i[-3])
    
    if (review_max[movie_name] == max_reviews) and (movie_name not in repeated_movies):
        movies_clean.append(i)
        repeated_movies.append(movie_name)
        
len(movies_clean)




# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en=movies_lang(movies_clean,3,'en')

# Call the rate_bucket function to see the movies with rating higher than 8.
movies_above_8=rate_bucket(movies_en,8,10)
