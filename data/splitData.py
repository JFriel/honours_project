file = open('todayinhistory.txt','r')
train = open('train.txt','w')
dev = open('dev.txt','w')
test = open('test.txt','w')

content = file.readlines()

count =0;
for i in content:
	if(count == 0):
		train.write(i)#train
	elif (count == 1):
		dev.write(i)#dev
	else:
		test.write(i)#test
	count +=1
	if(count == 10):
		count = 0;
	

train.close()
dev.close()
test.close()
file.close()


