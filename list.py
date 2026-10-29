# employee=["John","Smith","David","Peter"]
# for i in employee:
#     print(f"{i} is a good employee")



#     employee=["John","Smith","David","Peter"]
# for i in employee:
#     print(f"{i} is a good employee")
#     if i=="David":
#         print(f"{i} is a good employee and he is a team leader")
#         employee=["John","Smith","David","Peter"]
# for i in employee:
#     print(f"{i} is a good employee")
#     if i=="David":
#         print(f"{i} is a good employee and he is a team leader")    

        my_list=["Shubham","John", "27", "28", "29", "30", "31", "32", "33", "34", "35"]
        my_list.append("Shubham")  
        for i in my_list:
            print(f"{i} is a good employee")    
            print(f"The length of the list is: {len(my_list)}")   

            if(i>50):
                print(f"{i} is a good employee and he is a team leader")
                for i in my_list:
                    print(f"{i} is a good employee")    
                    print(f"The length of the list is: {len(my_list)}") 
