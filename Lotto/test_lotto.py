from lotto import random_num 

def test_random_num():
    #given
    #when
    for _ in range(10):
        numbers = sorted(random_num())
        
        #then
        assert len(numbers) == 6
        assert numbers[0] >= 1
        assert numbers[-1] <= 49

