#---设置代码运行的文件路径------

#cd D:\Mongo\bin
#mongod  -dbpath D:/Mongo/data/db 打开mongo数据库
setwd("F:\\学习\\量化学习\\策略代码")

#---加载调用Mongo数据库的包
library(quatitive)

#---更新股票基本面信息
stockcode=code("code")

#---更新股票交易历史数据和K线数据
updata(stockcode[,1])


#------------------------------计算相关技术指标的函数--------------------------

#计算今天开始前n天的移动平均线
get_MA1=function(x,n){
  len=length(x)
  MA1=NULL
  for(i in 1:len){
    if(i<=n){
      MA1[i]=sum(x[1:i])/i
    }else{
      s=i-n+1
      MA1[i]=sum(x[s:i])/n
    }
  }
  return(MA1)
}


#计算今天开始前n天的指数平滑移动平均

get_EMA1=function(close,n){
  len=length(close)
  EMA1=NULL
  ema1=get_MA1(close,n)
  for(i in 1:len){
    if(i<=n){
      EMA1[i]=ema1[i]
    }else{
      EMA1[i]=(2*close[i]+(n-1)*EMA1[i-1])/(n+1)
    }
  }
  return(EMA1)
}

#-----------------------------遍历所有股票，根据基本面信息和技术均线选股

ilen=1
EMA1=NULL
EMA2=NULL
relcode=NULL
relname=NULL
reltime=NULL
relstate=NULL
n=0
stockcodes=as.character(stockcode[,1])                                          #从基本面数据中提取全部股票代码
while (ilen<=length(stockcodes)&ilen<4000) {
  basic=get_basic_inf(stockcodes[ilen])                                         #给定股票代码提取基本面信息
  if(basic$pe<0|basic$pe>50|basic$outstanding!=basic$totals|basic$profit<=10){  #选择0<pe<50;流通股本=总股本；利润大于10亿的股票
    ilen=ilen+1
    next
  }
  dat=get_k_data(stockcodes[ilen])                                              #给定股票代码，提取K线数据
  if(length(dat[,1])<30){                                                       #剔除近一个月上市的新股
    ilen=ilen+1
    next
  }
  EMA1=get_EMA1(dat[,4],9)                                                      #计算第一期指数移动平滑平均
  EMA2=get_EMA1(EMA1,9)                                                         #计算第二期指数移动平滑平均
  Kp=NULL
  for(i in 1:length(EMA2)){
    if(i==1){
      Kp[i]=0
    }else{
      Kp[i]=(EMA2[i] - EMA2[i - 1]) / EMA2[i - 1] * 1000                        #遍历计算控盘值
    }
  }
  j=600
  while (j<=length(Kp)-7) {
    if(Kp[j]>0 & Kp[j-1]<0){                                                    #寻找金叉
      n=n+1
      if(dat[j+7,4]/dat[j,4]>1.05){                                             #选择一周增长超过5%的股票
        relcode[n]=stockcodes[ilen]
        relname[n]=as.vector(stockcode[ilen,2])
        reltime[n]=as.vector(dat[j,1])
        relstate[n]="OK"
      }else{
        relcode[n]=stockcodes[ilen]
        relname[n]=as.vector(stockcode[ilen,2])
        reltime[n]=as.vector(dat[j,1])
        relstate[n]="Failed"

      }
    }
    j=j+1
  }
  ilen=ilen+1
  print(ilen)
}
real=data.frame(relcode,relname,reltime,relstate)
select=real[which(real$relstate=="OK"),]
#K线图绘制
dat=get_k_data(as.character(select$relcode[2]))
candleplot(dat,40)
addMACD()
addSMA(5,col="red")
addSMA(10,col="blue")
addSMA(30,col="black")

