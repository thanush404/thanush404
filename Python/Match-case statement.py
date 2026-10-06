#                           Match-case statement (switch): An alternative to using many 'elif' statements
#                           Execute some code if a value matches a 'case'
#                           Benefits: cleaner and syntax is more readable


# def day_of_week(day):
#     match day:
#         case 1:
#             return 'It\'s Sunday!'
#         case 2:
#             return 'It\'s Monday!'
#         case 3:
#             return 'It\'s Tuesday!'
#         case 4:
#             return 'It\'s Wendsday!'
#         case 5:
#             return 'It\'s Thursday!'
#         case 6:
#             return 'It\'s Friday!'
#         case 7:
#             return 'It\'s Saturday!'

#         case _:                                      # use this with a space and '_' for else statesment
#             'It\'s not a valid day'
        
# print(day_of_week(2))        





def is_weekend(day):
    match day:
        case 'Saturday' | 'Sunday':
            return True
        case 'Monday' | 'Tuesday' | 'Wendsday' | 'Thursday' | 'Friday':
            return False
        case _:      
            return False
        
print(is_weekend('Sunday'))        