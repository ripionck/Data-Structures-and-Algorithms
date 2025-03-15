def maxNumberOfBalloons(text:str) -> int:
    # Frequency dixtionary for the text
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    # Calculate the maximum instances of "balloon"
    min_instances = float('inf')
    min_instances = min(min_instances, freq.get('b', 0))
    min_instances = min(min_instances, freq.get('a', 0))
    min_instances = min(min_instances, freq.get('l', 0) // 2)
    min_instances = min(min_instances, freq.get('o', 0) // 2)
    min_instances = min(min_instances, freq.get('n', 0))
    
    return min_instances

text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))