class Agent:
    prime=1.04
    def __init__(self,name,lastName,pay):
        self.name=name
        self.lastName=lastName
        self.pay=pay
    def FullName(self):
        return'{},{}'.format(self.name,self.lastName)
    def GivePrime(self):
        self.pay=self.pay*self.prime

class Dev(Agent):
    prime=1.1
    def __init__(self,name,lastName,pay,prog_lan):
        Agent.__init__(self,name,lastName,pay)
        self.prog_lan=prog_lan
class Manager(Agent):
    def __init__(self,name,lastName,pay,agents=None):
        Agent.__init__(self,name,lastName,pay)
        if agents is None:
            self.agents=[]
        else :
            self.agents=agents
    def add_agent(self,age):
        if age not in self.agents:
            self.agents.append(age)
    def remove_agent(self,age):
        if age in self.agents:
            self.agents.remove(age)
    def print_emp(self):
        for a in self.agents:
            print("-->",self.agents[a])
        


Age1=Agent("Mouad","Akharraz",120000)
Dev2=Dev("Maad","1007",122000,"Python")
Man3=Manager("Mx","Payne",150000,[Dev2])
Man3.print_emp()


