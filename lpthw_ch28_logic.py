""" Process to solve logic steps
1. Find an equality test (== or !=) and replace it with its truth
2. Find each and/or inside parentheses and solve those first
3. Find each not and invert it
4. Find any remaining and/or and solve it
5. When you are done you should have True or False
"""

answers = {
    1: True, 
    2: False,
    3: False,
    4: True,
    5: True,
    6: True,
    7: False,
    8: True,
    9: False,
    10: False,
    11: True,
    12: False,
    13: True,
    14: False,
    15: False,
    16: False,
    17: True,
    18: True,
    19: False,
    20: False
}

questions = {
    1: True and True,
    2: False and True,
    3: 1==1 and 2==1,
    4: "test" == "test",
    5: 1==1 or 2 !=1,
    6: True and 1==1,
    7: False and 0 != 0,
    8: True or 1 == 1,
    9: "test" == "testing",
    10: 1 != 0 and 2 == 1,
    11: "test" != "testing",
    12: "test" == 1,
    13: not (True and False),
    14: not (1==1 and 0!=1),
    15: not (10 ==1 or 1000==1000),
    16: not (1 !=10 or 3 ==4),
    17: not ("testing" == "testing" and "Zed" == "cool guy"),
    18: 1==1 and (not ("testing" ==1 or 1==0)),
    19: "chuncky" == "bacon" and (not (3==4 or 3==3)),
    20: 3==3 and (not ("testing" == "testing" or "Python" == "Fun"))
}


for key in questions:
    if answers[key] == questions [key]:
        print (f"{key} - correct")
    else:  
        print (f"{key} - wrong")
        print (f"Question answer is {questions[key]}") 

