def regularExpressionMatching(s, p):
	sindex = []
	p = list(p)
	s = list(s)
	for i in range(0,len(p)):
		if p[i] == "*":
			sindex.append(i)

	lack = 0
	if len(sindex)>=12:
		for i in range(0,len(sindex)-1):
			if p[sindex[0]-1-lack]==p[sindex[1]-1-lack]:
				sindex.pop(0)
				p.pop(0)
				p.pop(0)
				lack = lack + 2

	sindex = []
	for i in range(0,len(p)):
		if p[i] == "*":
			sindex.append(i)



	if len(sindex)==0:
		if len(s) != len(p):
			return False
		else:
			for i in range(0,len(s)):
				if s[i]!=p[i] and p[i]!=".":
					return False
			return True

	expend = len(s) - len(p) + 2*len(sindex)

	dic = []
	comb(expend,len(sindex),[],dic)

	n = len(sindex)
	ns = len(s)

	for i in range(0,len(dic)):
		newp = p[:sindex[0]-1]
		for j in range(0,n):
			newp = newp + [p[sindex[j]-1]]*dic[i][j]
			if j != n-1:
				newp = newp + p[sindex[j]+1:sindex[j+1]-1]
		newp = newp + p[sindex[n-1]+1:]

		

		checker = True
		for j in range(0,ns):
			if newp[j] != s[j] and newp[j] != ".":
				checker = False
				break
		if checker == True:
			return True

	return False

def comb(numobj,indices,cur,dic):
	if indices == 1:
		dic.append(cur+[numobj])
		return 0
	newcur = list(cur)
	for i in range(0,numobj+1):
		comb(numobj-i,indices-1,cur+[i],dic)
	return 0
