sentinel = 'œ' #a character that will never be in the program

buffer_1 = [100] #we will NOT be needing something as long as 4096 atm.
buffer_2 = [100]

lexemeBegin = None
forward = None

def start_state():
    return 0

x = 'x'

buffer_1 = ['A', ' ', ' = ', '(', '1', ',', '2', ')', ' ', ' (', '1', '2', ')']
class dfa_state:
    def __init__(self, state_number, accepting_state_b, incoming_char = None):
        self.state_num = state_number
        self.accepting_state_bool = accepting_state_b
        self.incoming_symbol = incoming_char

class dfa:
    def __init__(self, cur_state_u):
        self.cur_state = cur_state_u#reference an actual node
        self.states=[]

    def update_cur_state(self, cur_node):
        self.cur_state = cur_node

    def find_cur_state(self):
        return self.cur_state
    
    def append_state()

def determine_equal(input_stream):
    state_start = dfa_state(start_state(), False, None)
    find_equal = dfa(state_start)
    
    #define all non-starting states, including accepting state
    accepting_state = dfa_state(start_state(), True, '=')
    
    for c in input_stream:
        if (c == '='): 


            find_equal.update_cur_state(accepting_equal)
    
    if((find_equal.find_cur_state()) == '=')
    return 'x'#if x is a keyword

        

#we need to send in a character