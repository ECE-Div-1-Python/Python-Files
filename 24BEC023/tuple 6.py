def tuple6 ():
 original_tuple = (1, 2, 3, 4)
 temp_list = list(original_tuple)
 temp_list[1] = 99
 modified_tuple = tuple(temp_list)

 print("Original tuple:", original_tuple)
 print("Modified tuple:", modified_tuple)

tuple6 ()
