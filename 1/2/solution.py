# Open the file
with open('input.txt', 'r') as f:
    # Read the file contents and split them to lines
    content = f.read().strip().split('\n')
    results = [0]

    # Iterate over the list of lines
    for item in content:
        if item == '':
            # If the line is empty, append another item to results
            results.append(0)
        else:
            # If the line contains a number, add it to the last item in the results
            results[-1] += int(item)

    # Declare the array of the top three results
    top_three = [0, 0, 0]

    # Append each item, sort the list and then remove the lowest one
    # Do this for every result
    for result in results:
        top_three.append(result)
        top_three.sort(reverse=True)
        top_three.pop()

    # Print the sum of the top-three list
    print(sum(top_three))
