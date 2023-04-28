'''A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between.
 A balanced delimiter may contain any number of balanced delimiters.

Examples

The following are examples of balanced delimiter strings:
()[]{}
([{}])
([]{})

The following are examples of invalid strings:
([)]
([]
[])
([})
Input is provided as a single string. Your output should be True or False according to whether the string is balanced.

For example:
Input:
([{}])
Output:
True
'''

def balanced_delimeter():
    user_inp=input('enter the paranthesis: ')
    d={'(':')', '{':'}', '[':']'}
    stack=[]

    i=0
    while i<len(user_inp):
        if user_inp[i] in d.keys():
            stack.append(user_inp[i])
        elif user_inp[i] in d.values():
            if not stack:
                return False
            elif d[stack.pop()]!=user_inp[i]:
                return False
        i+=1

    return len(stack)==0

print(balanced_delimeter())