import os
import trim

'''
    reads in file from file path as a string, removes single line comments,
    block comments and condenses white spaces.
    returns the cleaned version
'''
def read_string_clean(path_to_file):

    buffer_size = 2048
    file_as_string = ""
    with open(path_to_file, 'r') as source_code:
        while True:
            file_read_buffer = source_code.read(buffer_size)
            if not file_read_buffer: 
                break

            file_as_string += file_read_buffer


    removed_single_comment = ''.join(trim.trim_single_comment(file_as_string))
    removed_white_space = ''.join(trim.trim_white_space(removed_single_comment))
    removed_block_comment = ''.join(trim.trim_block_comment(removed_white_space))

    return removed_block_comment


