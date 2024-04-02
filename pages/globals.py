
# Define your global variables here
user = None
selected_movie = None

# Function to set the value of user
def set_user(value):
    global user
    user = value

# Function to set the value of temp
def set_selected_movie(value):
    global selected_movie
    selected_movie = value

# Function to get the value of user
def get_user():
    
    return user

# Function to get the value of selected_movie
def get_selected_movie():
    return selected_movie
