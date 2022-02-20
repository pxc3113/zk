import os

NO_INSTANCES=3
for i in range(NO_INSTANCES):
    os.system("tar -xvf ~/Downloads/apache-zookeeper-3.7.0-bin.tar.gz && mv apache-zookeeper-3.7.0-bin zk"+str(i))
    os.system("mv zk"+str(i)+"/conf/zoo_sample.cfg zk"+str(i)+"/conf/zoo.cfg")
    os.system("touch zk"+str(i)+"/myid")
    f = open("zk"+str(i)+"/myid","a")
    f.write(str(i))
    f.close()

    f = open("zk"+str(i)+"/conf/zoo.cfg","a")
    for i in range(NO_INSTANCES):
        f.write("server."+str(i)+"=localhost:2181:3888\n")
    f.close()

s=[]
for i in range(NO_INSTANCES):
    s.append("sh ~/zk/zk"+str(i)+"/bin/zkServer.sh start")
    os.system(" && ".join(s))