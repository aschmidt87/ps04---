def languagefrequency(filename):
    with open(filename, encoding = 'utf-8') as file_object:
        contents = file_object.read()
    s = contents.split()
    list =[]
    for word in s:
        x = word.lower().strip('¡¿!-?¡#“_.:')
        list.append(x)
        
    counts ={}
    for word in list:
        if not word in counts:
            counts[word] =0
        counts[word] += 1
    
    sorted_counts = sorted(counts.items(), key = lambda kv: kv[1], reverse = True)
    
    most_frequent = dict(sorted_counts[:11])
    
    for word in most_frequent.keys():
        most_frequent[word] = most_frequent[word]/len(sorted_counts)
    
    return most_frequent


english = languagefrequency('eaton-boy-scouts_EN.txt')
spanish = languagefrequency('cherbonnel-mi-tio_SP.txt')
german = languagefrequency('schloemp-tolle-koffer_DE.txt')
unknown = languagefrequency('unknown-lang.txt')
    
s = 0
for u in unknown.keys():
    sp = spanish.get(u,0)
    u = unknown.get(u,0)
    sp_dif=abs(sp-u)
    s = sp_dif + s

print ("this is the unknown's difference with Spanish", s)
    
e  = 0
for u in unknown.keys():
    en = english.get(u,0)
    u = unknown.get(u,0)
    eng_dif=abs(en-u)
    e = eng_dif + e
print ("this is the unknown's difference with English", e)

g = 0
for u in unknown.keys():
    u= unknown.get(u,0)
    ger = german.get(u,0)
    germ=abs(ger-uk)
    g = germ + g
    
print ("this is the unknown's difference with German", g)

if s < e and s < g:
    print("Spanish!")
elif g < e and g < s:
    print('German!')
else:
    print('English')

    

##My prediction is that the unknown language is Spanish. This is proved by the code provided.

    
