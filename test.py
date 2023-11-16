import random
"""
json = '{\"tags\": ['
comma = ','
end = ']}'

count = random.randint(1, 5)
for _ in range(count):
    tagId = random.randint(1, 10)
    json += str(tagId)
    if(_ + 1 != count):
        json += comma
    
json += end
print(json)

"""

eb = 'eb'
mn = 1
for i in range(10):
    print(eb + str(mn).zfill(4))
    mn += 1
