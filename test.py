class Score:
    def __init__(self,chinese = None,english = None,math = None):
        self.chinese = chinese
        self.english = english
        self.math = math

    def caculate_avg(self):
        count = 0
        avgsum = 0
        if self.chinese != None:
            count += 1
            avgsum += self.chinese 
        if self.english != None:
            count +=1
            avgsum += self.english
        if self.math != None:
            count += 1
            avgsum += self.math
        
        if count != 0:
            return  (avgsum/count)
        else:
            return None

scoreA = Score(chinese = 20,english =30,math = 50)
print(scoreA.caculate_avg)

