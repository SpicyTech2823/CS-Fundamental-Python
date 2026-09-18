queue = []
queue.append(10)
queue.append(15)
queue.append(20)

print("Queue after adding elements:", queue)
# front element
print("Front element:", queue[0])
# removing elements
removed_element = queue.pop(0)
print("Removed element:", removed_element)
print("Queue after removing an element:", queue)
# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))
