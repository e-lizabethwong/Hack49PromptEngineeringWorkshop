import apikey
import cohere

co = cohere.Client(apikey.cohere_key)

message = "what is the cardinality of the smallest equivalence relation on {1, 2, 3} that contains (1, 2) and (2, 3)"

response = co.chat(
	message,
	model="command",
	temperature=0.9
)

answer = response.text
print(answer)