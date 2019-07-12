from sklearn import preprocessing

class Models:
    ss_x = preprocessing.StandardScaler()
    ss_y = preprocessing.StandardScaler()
    
    def __init__(self,ss_x=ss_x):
        pass

    #preprocess data
    def preprocess_data(self):
        path=os.getcwd()
        data=[]
        lines=open(path+'/blog/tmp_file/history.txt').readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].split(' ')
            data.append(lines[i][0])
            lines[i]=list(map(float,lines[i][1:-2]))
        train, target = [], []
        for j in range(len(lines)-30):
            tmp=[]
            for i in range(j,j+30):
                tmp+=lines[i]
            train.append(np.array(tmp))
            target.append(lines[j+30][2])
        remain_predict=[]
        five_test,five_true=[],[]
        for k in range(j+1,j+31):
            remain_predict+=lines[k]
        for i in range(len(lines)-35,len(lines)-30):
            tmp=[]
            for v in range(i,i+30):
                tmp+=lines[v]
            five_test.append(np.array(tmp))
            five_true.append(lines[i+30][2])
        for i in range(-5,0):
            data[i]=data[i][data[i].index('-')+1:]
        year_test,year_true,base=[],[],[]
        try:
            for i in range(len(lines)-275,len(lines)-30):
                tmp=[]
                for v in range(i,i+30):
                    tmp+=lines[v]
                year_test.append(np.array(tmp))
                year_true.append(lines[i+30][2])
                base.append(lines[i+29][2])
        except:
            pass
        return np.array(train),np.array(target),np.array(remain_predict),np.array(five_test),np.array(five_true),lines[-1][2],data[-5:],np.array(year_test),year_true,base
