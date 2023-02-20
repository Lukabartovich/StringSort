# StringSort
library for sorting strings on python.

Here are some examples:

    from StringSort import StringSort
    
    string = '(1, 3. 5, 2 /7]'
    
    sort = StringSort(string)
    sorted_string = sort.delete('(,./]')
    print(sorted_string)
