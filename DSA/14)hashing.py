# Function to display the hash table
def display_hash(hashTable):  
    for i in range(len(hashTable)):  
        print(i, end=" ")
        for j in hashTable[i]:  
            print("-->", j, end=" ") 
        print()  

# Create a hash table with 10 empty lists
HashTable = [[] for _ in range(10)]   

# Function to calculate the hash key
def Hashing(keyvalue):  
    return keyvalue % len(HashTable)   

# Function to insert a key-value pair into the hash table
def insert(Hashtable, keyvalue, value):  
    hash_key = Hashing(keyvalue)  
    Hashtable[hash_key].append(value)  

# Insert key-value pairs into the hash table
insert(HashTable, 10, 'Allahabad')  
insert(HashTable, 25, 'Mumbai')  
insert(HashTable, 20, 'Mathura')  
insert(HashTable, 9, 'Delhi')  
insert(HashTable, 21, 'Punjab')  
insert(HashTable, 21, 'Noida')  

# Display the hash table
display_hash(HashTable)
