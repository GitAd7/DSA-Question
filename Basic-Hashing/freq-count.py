def frequencyCount(self, arr):
        n = len(arr)
        count = {i: 0 for i in range(1, n+1)} # Step-01: Making a dictionary for pre-storing
        for i in arr:
            if i in count:
                count[i] += 1 #Step-02: Increasing count of that particular number, based on query
                
        return [count[i] for i in range(1, n+1)] # converting back to string