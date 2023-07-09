from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I've been waiting for a HuggingFace course my whole life.")
print(res)
res = classifier("I hate idiots.")
print(res)
res = classifier("I love flowers.")
print(res)
res = classifier("I'm feeling lower than normal.")
print(res)