from multiprocessing import Pool

def job(num):
    return num * 2
def job2(num):
    return "This: {}".format(num)

if __name__ == '__main__':
    p = Pool(processes=20)
    p2 = Pool(processes=45)
    data = p.map(job, [i for i in range(20)])
    data2 = p2.map(job2, [i for i in range(15)])
    p.close()
    p2.close()
    print(data, data2)
