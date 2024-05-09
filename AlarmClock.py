# Import necessary modules
import time
from playsound import playsound

# Define constants for clearing the screen using escape sequences
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Function to get the desired time from the user
def get_time():
    # Prompt user to input minutes and seconds
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    
    # Calculate total time in seconds
    global total_seconds
    total_seconds = minutes * 60 + seconds

    return total_seconds

# Function to run the alarm
def alarm(seconds):
    elapsed_time = 0
    
    # Clear the screen
    print(CLEAR)

    # Loop until elapsed time equals total time
    while elapsed_time < seconds:
        time.sleep(1)
        elapsed_time += 1

        # Calculate remaining time
        time_left = seconds - elapsed_time
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm in: {minutes_left:02d}:{seconds_left:02d}")
        
    # Play the alarm sound
    playsound("Akatsuki.mp3")

get_time()
alarm(total_seconds)