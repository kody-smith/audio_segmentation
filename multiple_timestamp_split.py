from pydub import AudioSegment

# Input file name
file_name = input("What is the name of the file you want to transcribe? ")

audio = AudioSegment.from_wav(file_name)

#Create an empty list of timestamps to be added by the user
list_of_timestamps = []

# enter the number of timestamps to add
n = int(input("Enter the number of splits you would like: "))
#Test for valid input

if n == None:

    print("Please enter a number.")

    n = int(input("Enter the number of splits you would like: "))

elif n <= 0:

    print("Invalid number of entries. Please enter a number greater than 0.")

    n = int(input("Enter the number of splits you would like: "))




else:

    #Iterate through the range

    for i in range(0,n):

        timestamp = int(input("What are the timestamps you want to split on (in seconds): "))

        list_of_timestamps.append(timestamp)

def split_files(time_list,file):

    start=0

    for i,t in enumerate(time_list):

        #End loop if you reach the end of the list

        if i == len(time_list):

            break

        end = t * 1000 # Convert to seconds

        start_rounded = int(start/1000)
        end_rounded = int(end/1000)

        print(f"Split at [{start_rounded}:{end_rounded}] sec")

        chunk = file[start:end]
        #a
        chunk.export(f"{file_name}_{end_rounded}.wav", format="wav")

        start = end 


split_files(list_of_timestamps,audio)
# Defects found: The files that are exported are blank, aka they do not have any audio to play through.
# Resolved: Needed to convert from milliseconds to seconds 


# Things to add:

# 2. Add Error handling

# Notes from Doug:
# Add split calls back together to make one whole call that flows.