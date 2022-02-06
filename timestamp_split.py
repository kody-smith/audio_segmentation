from scipy.io import wavfile
from pydub import AudioSegment

# Input file name
file_name = input("What is the name of the file you want to transcribe? ")

# convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3(file_name)
# sound.export(file_name, format="wav")

# Enter the timestamp to split at 
time_stamp = int(input("What time stamp do you want to split at? (seconds): "))

# Read the file and get the sample rate and data
rate, data = wavfile.read(file_name)

# Get the frame to split at
split_frame = rate * time_stamp

# Split the recordings
left_split, right_split = data[:split_frame-1], data[split_frame:]

# save the results into separate files
left_file = input("What would you like to name the first file? ")
right_file = input("What would you like to name the second file? ")
wavfile.write(left_file, rate, left_split)
wavfile.write(right_file, rate, right_split)