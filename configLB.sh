sudo chmod +x configLB.sh
sudo lxc-attach --clear-env -n lb -- sudo apt-get update
sudo lxc-attach --clear-env -n lb -- sudo apt-get install haproxy
sudo scp configHAProxy.py root@lb:/root
sudo lxc-attach --clear-env -n lb -- sudo python3 /root/configHAProxy.py

