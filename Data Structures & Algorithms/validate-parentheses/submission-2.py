class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {       
            "]" :"[",
            "}" : "{",
            ")" : "("
           
            }


        for elm in s:
            if elm in d:
                if stack and stack[-1] == d[elm]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(elm)


        if len(stack) > 0:
            return False
        else:
            return True




       
        
       

        
        
        
                

           


        

    


    



        