from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    roster = LinkedList()
    

    # 2) Insert some sample employee IDs.
    # insert_at_end preserves order -> 101 -> 102 -> 103 -> 104
    for emp_id in (101, 102, 103, 104):
        roster.insert_at_end(emp_id)
    
    # 3) Display the list to verify insertion
    roster.display()
    

    # 4) Call recursive_sum and print the result
    print(f"Sum of employee IDs: {roster.recursive_sum()}")
    

    # 5) Call recursive_search with a target and print result
    print(f"Search for 103: {roster.recursive_search(103)}")
    print(f"Search for 999: {roster.recursive_search(999)}")
    

    # 6) Call recursive_reverse, then display the reversed list
    roster.recursive_reverse()
    roster.display()
    


# 