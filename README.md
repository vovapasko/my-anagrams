# Anagrams finder

Searches and prints the anagrams of english words.

## How to run it? 
1. Clone this repository or download it and go to the root (my-anagrams/) folder.
2. Either run it using python on your PC (I was using python 3.8) or create your virtual environment if you wish.
Actually there are no dependencies used, so you probably won't need it.
3. To launch it, run `python main.py` command. In this case the default mock file will be attached. It is just for 
demonstration purposes. If you want to see all options, run `python main.py -h` command.
If you want you can either run `python main.py` command and default file will be set, or write an absolute path to the 
text file, you would like to parse. 
Pay attention that all words in file have to be split by the line separator.

## Concept
This program is divided by three parts:
1. Getting the information from the file.
2. Getting anagrams from that data.
3. Displaying it to the user.

Probably the most important is the part 2. The main idea is to iterate through each word, define it's semantic structure 
somehow unique and provide efficient grouping of the words. As we consistently need to fetch data from the storage, the 
best solution seems to be a hash map (O(1) reading). But the question is what should be the key and how to assign to the 
potential anagrams the same key. Let's say we have the word 'aabb'. In English there are 26 letters, so we can uniquely
define this word as following [2, 2, 0, 0, 0, ... 0], where size of this array is 26. In Python lists are not hashable, 
so we have to convert them to some hashable type. I chose the string for this purpose. If we have words 'aab', 'ab' and 'ba'
the structure for them looks like this:
```
{
    "[2, 1, 0, 0, ..., 0]": ["aab"],
    "[1, 1, 0, 0, ..., 0]": ["ab", "ba"],
} 
```

### Efficiency
- In this case key is always generated in the constant time - O(M), where M is the size of the word and using O(26) ~ O(1) 
memory, because it can't be bigger than the amount of letters in English alphabet.
- All anagrams are parsed in O(N) time, where N is the size of the given dataset. It needs O(N) memory, because in the 
worst case(there are no anagrams) it could be the hash map with N keys or the map with one key and list with N values 
(all words are anagrams).
