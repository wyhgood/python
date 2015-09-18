#!/bin/sh

function random(){ 
min=$1 
max=$(($2-$min+1)) 
num=$(cat /proc/sys/kernel/random/uuid | cksum | awk -F ' ' '{print $1}') 
echo $(($num%$max+$min)) 
}

starttime=$(date '+%s');

ports=(8080 8090 8123 9999);
max=50000;
timeout=6;
url=http://www.baidu.com/
ipcount=0;
vout=./result/$(date '+%Y%m%d%H%M%S').log;
vlog=./log.txt
usefulcount=0;

echo "">>${vlog};
echo "***********start scaning ip, now is $(date '+%Y-%m-%d %H:%M:%S')************">>${vlog};

function doScan(){
curr=0;
while ((curr++<${max})); do

ip=$(random 1 255)"."$(random 1 255)"."$(random 1 255)"."$(random 1 255);

for port in ${ports[@]};
do

ipport=${ip}":"${port};
echo "scan ip ${ipport}";
rcode=`curl --connect-timeout ${timeout} -X GET -x ${ipport} ${url} | grep -c 030173 2>/dev/null`

ipcount=$(expr ${ipcount} + 1);

if [ "${rcode}" = "1" ];then
usefulcount=$(expr ${usefulcount} + 1);
echo "${ipport} $(date '+%Y-%m-%d %H:%M:%S')">>${vout};
echo ">>>>>>>>>>find an useful ip ${ipport}">>${vlog};
fi

done

done;
}


tmp_fifofile="/tmp/$$.fifo"
mkfifo $tmp_fifofile
exec 6<>$tmp_fifofile
rm $tmp_fifofile

thread=1500;
for ((i=0;i<${thread};i++));do
echo
done >&6

while true
do
read -u6;
{
doScan && {
echo "a thread scan over.";
} || {
echo "a thread scan fail.";
}
echo >&6
} &
done

endtime=$(date '+%s');

echo "";
echo "";
echo "***************${ipcount} scan over, time used $(expr ${endtime} - ${starttime})s, find useful ip ${usefulcount}***************";
echo "";
echo "";
