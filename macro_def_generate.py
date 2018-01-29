fp1=open("macro_op.txt","w")
m_name=[]				#To store macro names
m_def=[]				#To store macro defination	
m_defnew=[]				#To store nested macro defination
m_start=[]				#To store macro starting Address
m_end=[]				#To store macro ending Address
m_label=[]				#To store macro label names
fp=open("macro.asm","r")
l=fp.readline()
q=0
n=2
while('section' not in l):		#split lines to store data in their list
	if(len(l)>1):
		if('%macro' in l):
			n=n-1
			t=0
			k=l.split()
			m_name.insert(0,k[1])
			m_start.insert(0,q)
			l=fp.readline()
			if('%%' in l):
				m_label.append(l)
			while('%endmacro' not in l):
				if('%macro' not in l):
					m_def.append(l)
				if('%macro' in l):
					n=n-1
					l=l.split()
					m_name.insert(0,l[1])
					l=fp.readline()
					if('%%' in l):
						m_label.append(l)
					while('%endmacro' not in l):
						m_defnew.append(l)
						t=t+1
						l=fp.readline()
				l=fp.readline()
				q=q+1
			if(n==0):
				m_end.insert(0,q-2)
				m_start.insert(0,q-1)
				m_end.insert(0,q+t-2)
				q=q+t-1
				n=2
				for i in m_defnew:
					m_def.append(i)
			else:
				n=2
				m_end.insert(0,q-1)
	l=fp.readline()

def check(a):					#calculate the index of macro name in the macro name list
	for i in range(len(m_name)):
		if(a==m_name[i]):
			return i

cnt=2
fp1.write(l)
l=fp.readline()
while(l!=""):
	if(len(l)>1):
		k=l.split()
		if (k[0] in m_name):
			z=check(k[0])
			z1=k[1].split(',')
			x=m_start[z]
			x1=m_end[z]
			while(x<=x1):
				if('%' in m_def[x] and '%endmacro' not in m_def[x] and '%macro' not in m_def[x]):
					if('%%' in m_def[x]):
						fp1.write('..@'+str(cnt)+'.'+(m_def[x])[:-1]+'\n')
						cnt=cnt+1	
					else:
						n=m_def[x].split()
						t=n[1].split(',')
						i=0
						while('%'+str(i) not in m_def[x]):
							i=i+1
						fp1.write("\t"+n[0]+" "+t[0]+","+z1[i-1]+"\n")
				else:
					if(len(m_def[x])>1):
						fp1.write(m_def[x])
				x=x+1
		else:
			fp1.write(l)
	l=fp.readline()

