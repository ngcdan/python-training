def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        # If you want to program fail slightly, you can use the following code:
        # pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = './python_crash_course/chapter_1/resources/alice.txt'
count_words(filename)