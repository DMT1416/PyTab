
import wikipedia

# Ask the user
question = input("Put your question here:  ")

# Try to get a summary from Wikipedia
try:
    summary = wikipedia.summary(question, sentences=2)
    print("Answer:", summary)
except wikipedia.exceptions.DisambiguationError as e:
    print("Too many possible answers. Be more specific.")
except wikipedia.exceptions.PageError:
    print("Sorry, I couldn’t find anything on that.")
