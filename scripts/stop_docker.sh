#!/bin/bash
docker_id=`docker ps |grep -v 'system' | grep " Up 6 days" | awk '{print $1;}'| sed -n '1p'`
if [ "$docker_id" != "" ]
then
	echo "暂停镜像:"
	docker stop $docker_id
fi	
