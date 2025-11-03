from transformers import pipeline
from colorama import Fore

sentiment = pipeline("sentiment-analysis")
text_a = "I like cars."
text_b = "I don't like cars."
text_c = "I like car but I don't like bike."

sentiment_a = sentiment(text_a)
print(Fore.RED + str(sentiment_a) + Fore.RESET)

sentiment_b = sentiment(text_b)
print(Fore.CYAN + str(sentiment_b) + Fore.RESET)

sentiment_c = sentiment(text_c)
print(Fore.GREEN + str(sentiment_c) + Fore.RESET)


print("\n\n")
generator = pipeline("text-generation", model="gpt2")
generated = generator("Once upon a time", max_length=30, num_return_sequences=1)
print(generated)