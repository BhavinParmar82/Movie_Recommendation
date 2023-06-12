import os
import time

lock_file_path = './lock_file'

def acquire_lock():
    while os.path.exists(lock_file_path):
        #print("Instance is already running. Please try again later.")
        time.sleep(5)  # Adjust the delay as per your requirements

    # Create the lock file
    with open(lock_file_path, 'w') as lock_file:
        lock_file.write('locked')

def release_lock():
    # Remove the lock file
    os.remove(lock_file_path)

# Acquire the lock
#acquire_lock()

# Release the lock when the application finishes
#release_lock()
