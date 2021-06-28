# Add the functions in this file
import json
def load_journal(s1):
	with open(s1) as f1:
		ob=json.load(f1)
	return ob
def compute_phi(s1,ev):
	ob=load_journal(s1)
	n11=0
	nee=0
	n1e=0
	ne1=0
	n1p=0
	nep=0
	np1=0
	npe=0
	for k in ob:
		if((ev in k['events']) and k['squirrel']==True):
			n11=n11+1
			n1p=n1p+1
			np1=np1+1
		elif((ev not in k['events']) and k['squirrel']==False):
			nee=nee+1
			nep=nep+1
			npe=npe+1
		elif((ev in k['events']) and k['squirrel']==False):
			n1e=n1e+1
			n1p=n1p+1
			npe=npe+1
		elif((ev not in k['events']) and k['squirrel']==True):
			ne1=ne1+1
			nep=nep+1
			np1=np1+1
	q=(n1p*nep*np1*npe)**(0.5)
	m=(n11*nee)-(n1e*ne1)
	a=m/q
	return a
def compute_correlations(s1):
	ob=load_journal(s1)
	u=set()
	for k in ob:
		l=k['events']
		for i in l:
			u.add(i)
	d=dict()
	for j in u:
		d[j]=compute_phi(s1,j)
	return d
def diagnose(s1):
	d=compute_correlations(s1)
	l1=d.values()
	a=max(l1)
	b=min(l1)
	l3=[]
	for i,j in d.items():
		if(j==a):
			l3.append(i)
		if(j==b):
			l3.append(i)
	l4=sorted(l3)
	return l4[1],l4[0]

