'''
--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic. "The printer's broken!
We can't print the Naughty or Nice List!" By the time you make it to sub-basement 17, there are only a
few minutes until midnight. "We have a big problem," she says; "there must be almost fifty bugs in this system,
 but nothing else can print The List. Stand in this square, quick! There's no time to explain; if you can convince
 them to pay you in stars, you'll be able to--" She pulls a lever and the world goes blurry.

When your eyes can focus again, everything seems a lot more pixelated than before. She must have sent you inside the
computer! You check the system clock: 25 milliseconds until midnight. With that much time, you should be able to
collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day millisecond in the advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door is locked,
but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove you're not a human. Apparently,
you only get one millisecond to solve the captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match
the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

    1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2)
    matches the fourth digit.
    1111 produces 4 because each digit (all 1) matches the next.
    1234 produces 0 because no digit matches the next.
    91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?
'''

class Node(object):
    ''' Node class for storing data with a next pointer.
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    ''' LinkedList container class.
    '''
    def __init__(self):
        self.head = None

    def insert(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = Node(item)

def create_linked_list(input_list):
    ''' Helper function to create linked list.
    '''
    ll = LinkedList()
    for item in input_list:
        ll.insert(item)
    return ll

def inverse_captcha(input_list):
    ''' Solution to inverse captcha.
        input_list: list of integers
    '''
    linked_list = create_linked_list(input_list)
    answer = 0

    head = linked_list.head
    current = head

    while current.next:
        if current.data == current.next.data:
            answer += current.data
        current = current.next

    # last check since the list is circular
    if current.data == head.data:
        answer += head.data

    return answer

if __name__ == '__main__':
    print(inverse_captcha([1, 1, 2, 2]))
    print(inverse_captcha([9, 1, 2, 1, 2, 1, 2, 9]))
    print(inverse_captcha([1, 1, 1, 1]))
    print(inverse_captcha([1, 2, 3, 4]))
