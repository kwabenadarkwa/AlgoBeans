from enum import Enum


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.bottom = None

    def is_empty(self):
        return self.head == None

    def insert_at_head(self, value):
        if self.head is None:
            self.head = ListNode(value)
        else:
            previous_head = self.head
            self.head = ListNode(value)
            self.head.next = previous_head

    def insert_at_tail(self, value):
        if self.head is None:
            self.head = ListNode(value)
        else:
            current_node = self.head
            while current_node and current_node.next:
                current_node = current_node.next
            current_node.next = ListNode(value)

    def remove_at_head(self):
        value = None
        if self.head and self.head.next:
            value = self.head.value
            self.head = self.head.next
        else:
            self.head = None
        return value if value else None

    def __str__(self):
        current_node = self.head
        return_string = ""
        while current_node:
            return_string += f" {current_node.value} ->"
            current_node = current_node.next
        return_string += "None"
        return return_string


# INFO:
# Animal Shelter. An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat.You may use the built-in LinkedList data structure


class AnimalType(Enum):
    CAT = 1
    DOG = 0


# refactor the remove from tail
class AnimalShelter:
    def __init__(self):
        self.dogs: SinglyLinkedList = SinglyLinkedList()
        self.cats: SinglyLinkedList = SinglyLinkedList()
        self.previous_animal: AnimalType = AnimalType.DOG

    def enqueue(self, animal_type: AnimalType, name):
        match animal_type:
            case AnimalType.CAT:
                self.cats.insert_at_tail(name)
            case AnimalType.DOG:
                self.dogs.insert_at_tail(name)

    #should have had some kind of animal class that stores what the order of the animal is 
    #because this one is supposed to bring the oldest out of the two not just select at randwom
    #perhaps if we were storing a class for an amimal we could have just passed the animal class to the eneuque also
    def dequeueAny(self):
        self.previous_animal = (
            AnimalType.DOG if self.previous_animal == AnimalType.CAT else AnimalType.CAT
        )
        return (
            self.dequeueDog()
            if self.previous_animal == AnimalType.DOG
            else self.dequeueCat()
        )

    def dequeueDog(self):
        dog_name = self.dogs.remove_at_head()
        return dog_name if dog_name else "No dog left in the shelter"

    def dequeueCat(self):
        cat_name = self.cats.remove_at_head()
        return cat_name if cat_name else "No cat left in the shelter"


if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(AnimalType.DOG, "akosua")
    animal_shelter.enqueue(AnimalType.DOG, "scooby")
    animal_shelter.enqueue(AnimalType.DOG, "browny")
    animal_shelter.enqueue(AnimalType.CAT, "peace")
    animal_shelter.dequeueCat()
    animal_shelter.dequeueCat()
    animal_shelter.dequeueDog()
    animal_shelter.dequeueDog()
    animal_shelter.dequeueDog()
    print(animal_shelter.cats)
    print(animal_shelter.dogs)
