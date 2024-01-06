# Chaining Hash Table. Source Citation: W-1_ChainingHashTable_zybooks_Key_Value.py
class ChainingHashTable:
    def __init__(self, initial_capacity=20):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    
    # Inserts and updates new items into the hash table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table) # Takes the key and mod the length of hash table
        bucket_list = self.table[bucket] 
        
        # Update key if is already in the bucket
        for kv in bucket_list: # This searches the entire list
            if kv[0] == key: # If the updated key name matches a name in the list at 0 index
                kv[1] = item # Value pair of key is updated at 1 index
                return True
            
        # Not in a bucket then must be new and appended to the list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
    
    # Searches the items in hash table
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None 
    
    # Removes key in the hash table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        if key in bucket_list:
            bucket_list.remove(key) # Removes key if in list