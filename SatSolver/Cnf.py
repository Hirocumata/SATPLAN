class Solution(object):
	"""docstring for Solution"""
	def __init__(self, success=False, var_sol={}):
		self.success=success
		self.var_sol=var_sol

	def __getitem__(self, i):
		if i in self.var_sol.keys():
			return self.var_sol[i]
		else:
			return None
	def __setitem__(self,idx,value):
		self.var_sol[idx]=value

class Variable(object):
	"""docstring for Variable"""
	def __init__(self, name, signal=True):
		self.name = name
		self.signal=signal

	def __eq__(self,other): #Ask mighty Gui for explanation here
		return (isinstance(other,self.__class__)) and other.name==self.name and other.signal==self.signal

	def __hash__(self):
		return hash(str(self.name) + str(self.signal))


class CNF(object):
	"""docstring for SatSolver"""
	def __init__(self, file_name):
		
		clauses, symbols = readCnf(file_name)

		self.clauses=clauses

		self.symbols=symbols


def readCnf(file_name):
	symbols=[]
	clauses=set([]) #Cant be frozen to be able to learn
	f=open(file_name)

	for line in f:
		if line[0]=='c':
			continue
		if line[0]=='p':
			words=line.strip("\n").split()
			for i in range(1,int(words[2])+1):
				symbols.append(i)
				#What to do with clauses number?
		else:
			if(line!="\n"):
				words=line.strip("\n").split()
				obj_list=[]
				for w in words:
					if w !="0":
						if w[0]=="-":
							obj_list.append(Variable(int(w[1:]),False))
						else:
							obj_list.append(Variable(int(w),True))

				clauses.add(frozenset(obj_list))
	f.close()

	return [clauses, symbols]