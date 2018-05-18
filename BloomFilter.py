
import math
import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        '''
            size :  int
                Size of the Bloom Filter
            hash_count : int
                No. of hash counts for the bloom filter
        '''  
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
    
        
    def add(self, item):
        '''
            item : object
                Item to be added to the filter
        '''
        for i in range(self.hash_count):  
            # i works as seed to mmh3.hash() function
            # With different seed, digest created is different
            index = mmh3.hash(item,i) % self.size
               
            # Setting the bit as True for the particular index generated
            self.bit_array[index] = True
            
    def check(self, item):
        '''
        Check for existence of an item in filter
        '''
        for i in range(self.hash_count):
            index = mmh3.hash(item,i) % self.size
            if self.bit_array[index] == False:
                # if the bit is False, it means that the word searched for does not exist. Return false.
                return False
        return True



%matplotlib inline
import random 
import string
import matplotlib.pyplot as plt

def randomword(length):
    #generates a random word of given length
    return ''.join(random.choice(string.lowercase) for i in range(length))

def theoretical_fp(array_size, inserts):
    array_size = float(array_size)
    inserts = float(inserts)
    k = (array_size/inserts)*math.log(2)
    p = (1 - (1 - (1/array_size))**(k*inserts))**k
    return p

def false_positives(array_size, hash_count, insertions):
    str_length = 10
    fp_array = []

    for num in insertions:
        bloom = BloomFilter(array_size, hash_count)
        fp_count = 0 #keeps track of false positive count
        #initializing an array of random words
        words = [randomword(str_length) for i in range(num)]
        words_present = words[:(num/2)]
        words_absent = words[(num/2):]

        for word in words_present:
            bloom.add(word)

        random.shuffle(words_present)
        random.shuffle(words_absent)

        for strng in words_absent:
            if bloom.check(strng) == True:
                fp_count += 1

        fp_array.append(fp_count/float(len(words_absent)))
    return fp_array

def average(array_size, hash_count, insertions):
    #store 3 different false positive rate arrays
    a = false_positives(array_size, hash_count, insertions)
    b = false_positives(array_size, hash_count, insertions)
    c = false_positives(array_size, hash_count, insertions)
    
    total = []
    for num in a:
        total.append(num)
    for i in range(len(b)):
        total[i] = total[i] + b[i] + c[i]
        total[i] = total[i]/3
    return total

def main():
    array_size = 1000
    hash_count = 5
    insertions = [num for num in range(1, array_size, 10)]
    theory = []
    #determining the theoretical false positive rate
    for x in insertions:
        theory.append(theoretical_fp(array_size, x))
        
    #determining the average false positive rate
    fp = average(array_size, hash_count, insertions) 
    
    #plotting the theoretical and actual false positives rates
    plt.plot(insertions, fp, label = 'Actual')
    plt.plot(insertions, theory, label = 'Theoretical')
    plt.xlabel("Number of elements")
    plt.ylabel("False Positive Rate")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
    
main()
main()
main()

