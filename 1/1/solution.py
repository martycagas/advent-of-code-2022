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

    # Print the highest number in the list
    print(max(results))
