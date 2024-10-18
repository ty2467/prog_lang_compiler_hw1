#helper functions for removing comments and white spaces
def trim_block_comment(input_string: str):

    out = []
    i = 0

    while i in range(len(input_string)): 
        if input_string[i] == '`': 
            if(i == len(input_string)-1):
                break
            i += 1

            while (input_string[i]!= '`' and i != len(input_string)-1 ):
                i += 1


            if(i == len(input_string)-1):
                break    

            i += 1

        out.append(input_string[i]) 

        i += 1
    return out


def trim_single_comment(input_string: str):
    out = []
    i = 0

    while i in range(len(input_string)): 
        if input_string[i] == '#': 
            if(i == len(input_string)-1):
                break
            i += 1

            while (input_string[i]!= '\n' and i != len(input_string)-1 ):
                i += 1
           
            if(i == len(input_string)-1):
                break


        out.append(input_string[i]) 

        i += 1 
    return out

def trim_white_space(input_string: str):
    new_list = []
    i = 0
    while i in range(len(input_string)):
        if input_string[i] != ' ' and input_string[i] != '\t' and input_string[i] != '\n':
            new_list.append(input_string[i])
        if input_string[i] == ' ' or input_string[i] == '\t' or input_string[i] == '\n': 

            if(i == len(input_string)-1): 
                new_list.append(input_string[i]) 
                break
            j=i+1

            while input_string[j] == ' ':
                if(j == len(input_string)-1):
                    new_list.append(input_string[j])
                    break
                    
                i += 1
                j += 1
            new_list.append(input_string[i])#has to preserve \n, for detecting line number
        i+=1
    return new_list