# Deema Mohammed AL-Maqadma
# LinkedList Assignment
# The Implementation
from LinkedList import LinkedList

def main():
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    # طباعة القائمة الأصلية
    print("\nLinkedList Befor Traversing : \n")
    ll.print_list()  # 1 -> 2 -> 3 -> 4 -> None 
    print()
    print("*"*50)
    # عكس القائمة
    ll.reverse()
    # ll.reverse_using_stack() او باستخدام الستاك
    # طباعة القائمة بعد العكس
    print("\nLinkedList After Traversing : \n")
    ll.print_list()  # 4 -> 3 -> 2 -> 1 -> None

# # Usage
if __name__ == "__main__":
    main()
print("\n---->>> Thx ^_^ <<<---- \n")
