import sys
import re

def make_clean_dataset(word_length: int, input_filename: str, output_filename: str) -> None:
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            while(line := input_file.readline().rstrip().lower()):
                if len(line) == word_length and bool(re.match("^[a-z]+$", line)):
                    output_file.write(f"{line}\n")
        print("Finished!")
    except Exception as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    try: 
        word_length = int(sys.argv[1])
        input_filename = sys.argv[2]
        output_filename = sys.argv[3]
        make_clean_dataset(word_length, input_filename, output_filename)
    except:
        print("Must provide word length, input and output filenames")
        exit(1)