import unittest
import cap
'''
In order to perform unittest, we create a script and a test script. 
In the test script we import unittest and the script that we want to test
We then create a class and inherit from unittest.TestCase
'''
class TestCap(unittest.TestCase):
    '''
    Inside the class we write methods to test our methods in script.
    For each method or function in our script we can write multiple 
    test functions.
    '''
    def test_one_word(self):
        '''
        The format of the method is simple
        we give it an input in this case text
        we define a variable hold the value returned after invoking our function
        then we assert that our result matches the result we expected
        It is important to note that first is the result from the function we invoked
        and then is the result we expect it to give us.
        This order is very important otherwise the test result will not be right.
        '''
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
    def test_multiple_words(self):
        '''
        Another method test case of our function
        '''
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
if __name__ == '__main__':
    unittest.main()
