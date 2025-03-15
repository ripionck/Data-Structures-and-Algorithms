from collections import Counter

def maxNumberOfBalloons(str):
    # Create a counter for all characters in text
    freq = Counter(text)
    
    # Calculate instances for ecch letter needed in 'balloon'
    b_count = freq['b']
    a_count = freq['a']
    l_count = freq['l'] // 2
    o_count = freq['o'] // 2
    n_count = freq['n']
    
    
    return min(b_count, a_count, l_count, o_count, n_count)

text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))
