'''
@author         
@date           mar 23 2023
@file           main.py
@brief          eecs 210 discrete structures assignment 5

@description    write a program that takes inputs A, B, and a relation f and 
                determines if the relation is a function or not 
                if it is a function determines whether it is injective, surjective, or bijective
                if it is bijective determines the inverse function
                your program should print out the inputs using the notation A = {...}. B = {...}, f = {(a, b), ...} 

@testing        test your program with the following inputs:

                1. A = {a,b,c,d}, B = {v,w,x,y,z}, f = {(a,z),(b,y),(c,x),(d,w)}
                2. A = {a,b,c,d}, B = {x,y,z}, f = {(a,z),(b,y),(c,x),(d,z)}
                3. A = {a,b,c,d}, B = {w,x,y,z}, f = {(a,z),(b,y),(c,x),(d,w)}
                4. A = {a,b,c,d}, B = {1,2,3,4,5}, f = {(a,4),(b,5),(c,1),(d,3)}
                5. A = {a,b,c}, B = {1,2,3,4}, f = {(a,3),(b,4),(c,1)}
                6. A = {a,b,c,d}, B = {1,2,3}, f = {(a,2),(b,1),(c,3),(d,2)}
                7. A = {a,b,c,d}, B = {1,2,3,4}, f = {(a,4),(b,1),(c,3),(d,2)}
                8. A = {a,b,c,d}, B = {1,2,3,4}, f = {(a,2),(b,1),(c,2),(d,3)}
                9. A = {a,b,c}, B = {1,2,3,4}, f = {(a,2),(b,1),(a,4),(c,3)}
'''


def main():
     
    test_cases = [

        (set("abcd"), set("vwxyz"),     {("a", "z"), ("b", "y"), ("c", "x"), ("d", "w")}),
        (set("abcd"), set("xyz"),       {("a", "z"), ("b", "y"), ("c", "x"), ("d", "z")}),
        (set("abcd"), set("wxyz"),      {("a", "z"), ("b", "y"), ("c", "x"), ("d", "w")}),
        (set("abcd"), set(range(1, 6)), {("a", 4), ("b", 5), ("c", 1), ("d", 3)}),
        (set("abc"),  set(range(1, 5)), {("a", 3), ("b", 4), ("c", 1)}),
        (set("abcd"), set(range(1, 4)), {("a", 2), ("b", 1), ("c", 3), ("d", 2)}),
        (set("abcd"), set(range(1, 5)), {("a", 4), ("b", 1), ("c", 3), ("d", 2)}),
        (set("abcd"), set(range(1, 5)), {("a", 2), ("b", 1), ("c", 2), ("d", 3)}),
        (set("abc"),  set(range(1, 5)), {("a", 2), ("b", 1), ("a", 4), ("c", 3)})
    ]
    
    for i, (A, B, f) in enumerate(test_cases, 1):
        
        print(f"test case:", i)
        print(f"A = {A}, B = {B}, f = {f}")

        if is_function(A, f):
            print("the relation is a function\n")
            injective = is_injective(f)
            surjective = is_surjective(B, f)
            bijective = injective and surjective
            
            if injective:
                print(f"the function is injective")

            if surjective:
                print("the function is surjective")

            if bijective:
                print("the function is bijective")

            elif not injective and not surjective:
                print("the function is neither injective nor surjective")

            elif not injective:
                print("the function is not injective")

            elif not surjective:
                print("the function is not surjective")

        else:
            print("the relation is not a function")

        print('\n')


def is_function(A, f):
    
    temp = set()
    
    for i, j, in f:
        if i in temp:
            return False
        else:
            temp.add(i)

    return (temp == A)

def is_injective(f):
   
    temp = set()

    for i, j in f:
        if j in temp:
            return True
        else:
            temp.add(j)
    return True

def is_surjective(B, f):
  
    temp = set()

    for i, j in f:
        temp.add(j)

    return (temp == B)

def inverse_function(f):
    return {(b, a) for a, b, in f}
    

if __name__ == "__main__":
    main()



