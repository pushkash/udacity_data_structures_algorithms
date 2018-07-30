class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        current = self.head

        if self.head:
            while current.next:
                current = current.next

            current.next = Element(value)

        else:
            self.head = Element(value)

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current_position = 1

        if position < 1:
            return None

        if self.head:
            current = self.head

            while current and current_position <= position:
                if current_position == position:
                    return current
                current = current.next
                current_position += 1

            return None

    def insert(self, position, element):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current_position = 1

        current = self.head

        if position > 1:
            while current and current_position < position:
                if current_position == position - 1:
                    element.next = current.next
                    current.next = element
                current = current.next
                current_position += 1
        elif position == 1:
            element.next = self.head
            self.head = element


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head

        # My solution
        # if self.head:
        #     while current.next:
        #         if current.next.value == value:
        #             break
        #         current = current.next
        #
        #     if current.next.next:
        #         current.next = current.next.next
        #     else:
        #         current.next = None


        #Udacity solution
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next

        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next



l_l = LinkedList()

for i in range(0, 100):
    l_l.append(i)

pos_el = l_l.get_position(5)

print(pos_el.value)

l_l.insert(6, Element('hh'))

pos_el = l_l.get_position(6)
print(pos_el.value)

l_l.delete('hh')

print(l_l.print_list())