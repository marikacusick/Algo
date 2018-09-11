# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from bloom_filter import BloomFilter

bfilter = BloomFilter()
bfilter.add_elem("example_elem")
if not bfilter.check_membership("example_elem"):
  print("bloom filter did not return True for added element ")

bloom = BloomFilter(100)
animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
           'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
           'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
# First insertion of animals into the bloom filter
for animal in animals:
    bloom.add_elem(animal)

    # Membership existence for already inserted animals
    # There should not be any false negatives
for animal in animals:
    if bloom.check_membership(animal):
        print('{} is in bloom filter as expected'.format(animal))
    else:
        print('Something is terribly went wrong for {}'.format(animal))
        print('FALSE NEGATIVE!')

                # Membership existence for not inserted animals
                # There could be false positives
other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
                                 'whale', 'shark', 'fish', 'turkey', 'duck', 'dove',
                                 'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla',
                                 'hawk' ]
for other_animal in other_animals:
    if bloom.check_membership(other_animal):
        print('{} is not in the bloom, but a false positive'.format(other_animal))
    else:
        print('{} is not in the bloom filter as expected'.format(other_animal))
