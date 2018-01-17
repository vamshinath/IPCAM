read -p "Enter date(MMDD):" dt
echo "Synching from camera"
sleep 2
#wget --user=admin  --password=vamshi81 -r -A "*.jpg" -np -nc "http://192.168.0.108/sd/2018$dt/" &
#wget --user=admin  --password=vamshi81 -r -A "*.jpg" -np -nc "http://192.168.0.108/sd/2018$dt/" &
wget -O data.txt --user=admin  --password=vamshi81  "http://192.168.0.108/sd/2018$dt/" 



folders=$(cat data.txt | grep "images*" | cut -f4 -d'/')

for x in $folders
do
wget -r -A "*.jpg" -np -nc "http://admin:vamshi81@192.168.0.108/sd/2018$dt/$x/" &
done
wait
python3 similarGroup.py 192.168.0.108/sd/2018$dt
mkdir $dt 
find 192.168.0.108/sd/2018$dt -type f ! -empty -exec cp {} $dt \;
