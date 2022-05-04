''' book store '''

import unittest

cost_of_a_book_dict = {
                        1: 800, 
                        2: 800 * 0.95, 
                        3: 800 * 0.9, 
                        4: 800 * 0.8,
                        5: 800 * 0.75
                      }

def count_repetitions(basket, books_count=5):
    basket_count_dict = {}
    for book in range(1, books_count + 1):
        basket_count_dict[book] = basket.count(book)
    return sorted(basket_count_dict.values())

def count_groups(counted_books):
    counted_groups, act_index = {}, 0
    while sum(counted_books) > 0:
        if counted_books[act_index] > 0:
            counted_groups[len(counted_books) - act_index] = counted_books[act_index]
            for index in range(act_index, len(counted_books)):
                counted_books[index] -= counted_groups[len(counted_books) - act_index]
        act_index += 1
    return counted_groups


def total(basket):
    counted_books = count_repetitions(basket)
    counted_groups = count_groups(counted_books)
    result = 0
    for key in sorted(counted_groups.keys(), reverse=True):
        if key - 2 in counted_groups.keys() and key == 5:
            count_of_mean_group = min(counted_groups[key], counted_groups[key-2])
            result += cost_of_a_book_dict[key - 1] * (key - 1) * count_of_mean_group * 2
            counted_groups[key] -= count_of_mean_group
            counted_groups[key - 2] -= count_of_mean_group
        result += cost_of_a_book_dict[key] * key * counted_groups[key]
    return result

    

class BookStoreTest(unittest.TestCase):
    def test_only_a_single_book(self):
        basket = [1]
        self.assertEqual(total(basket), 800)

    def test_two_of_the_same_book(self):
        basket = [2, 2]
        self.assertEqual(total(basket), 1600)

    def test_empty_basket(self):
        basket = []
        self.assertEqual(total(basket), 0)

    def test_two_different_books(self):
        basket = [1, 2]
        self.assertEqual(total(basket), 1520)

    def test_three_different_books(self):
        basket = [1, 2, 3]
        self.assertEqual(total(basket), 2160)

    def test_four_different_books(self):
        basket = [1, 2, 3, 4]
        self.assertEqual(total(basket), 2560)

    def test_five_different_books(self):
        basket = [1, 2, 3, 4, 5]
        self.assertEqual(total(basket), 3000)

    def test_two_groups_of_four_is_cheaper_than_group_of_five_plus_group_of_three(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(total(basket), 5120)

    def test_two_groups_of_four_is_cheaper_than_groups_of_five_and_three(self):
        basket = [1, 1, 2, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 5120)

    def test_group_of_four_plus_group_of_two_is_cheaper_than_two_groups_of_three(self):
        basket = [1, 1, 2, 2, 3, 4]
        self.assertEqual(total(basket), 4080)
        
    def test_two_each_of_first_four_books_and_one_copy_each_of_rest(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        self.assertEqual(total(basket), 5560)

    def test_two_copies_of_each_book(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 6000)

    def test_three_copies_of_first_book_and_two_each_of_remaining(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1]
        self.assertEqual(total(basket), 6800)
        
    def test_three_each_of_first_two_books_and_two_each_of_remaining_books(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2]
        self.assertEqual(total(basket), 7520)
        
    def test_four_groups_of_four_are_cheaper_than_two_groups_each_of_five_and_three(self):
        basket = [1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(total(basket), 10240)
        
    def test_check_that_groups_of_four_are_created_properly_even_when_there_are_more_groups_of_three_than_groups_of_five(self):
        basket = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 14560)

    def test_one_group_of_one_and_four_is_cheaper_than_one_group_of_two_and_three(self):
        basket = [1, 1, 2, 3, 4]
        self.assertEqual(total(basket), 3360)
        
    def test_one_group_of_one_and_two_plus_three_groups_of_four_is_cheaper_than_one_group_of_each_size(self):
        basket = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
        self.assertEqual(total(basket), 10000)

    def test_two_groups_of_four_and_a_group_of_five(self):
        basket = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]
        self.assertEqual(total(basket), 8120)          

    def test_shuffled_book_order(self):
        basket = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
        self.assertEqual(total(basket), 8120)
        
if __name__ == "__main__":
    unittest.main()
    