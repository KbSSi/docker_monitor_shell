#!/bin/bash
count=0
declare -A docker_id
#front_id=`docker stats --no-stream | grep -v 'system'| grep -v 'NAME'| awk '{if ($3 =="0.00%")print $1;}' | sed -n '1p'`
while true
do
	front_id=`docker stats --no-stream | grep -v 'system'| grep -v 'NAME'| awk '$3~/^[0]/{print $1;}'`
	sleep 6m
	for i in `docker stats --no-stream | grep -v 'system'| grep -v 'NAME'| awk '$3~/^[0]/{print $1;}'`
	do
		if [[ "$front_id" =~ "$i" ]];then
			let docker_id[$i]++
			#echo ${docker_id[$i]}
			if [ ${docker_id[$i]} -eq 90 ];then #模拟90次
				docker_id[$i]=0
				date >> ../logs/stop_docker_cpu.log
				echo "暂停镜像:" >> ../logs/stop_docker_cpu.log
				echo $i >> ../logs/stop_docker_cpu.log
                       		docker stop $i
			fi
		else
			docker_id[$i]=0
		fi
	done
done
