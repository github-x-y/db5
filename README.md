# db5
shell  repositor
#!/bin/bash
read -p "please enter your user name：" user
if [ -z $user ];then
echo "please enter your user name" 
exit 2
else
useradd $user > /dev/null
echo "User created successfully"
fi
stty -echo
read -p "Please enter your username and password:" pass
stty echo
pass=${pass:-123456}
echo "$pass" | passwd --stdin "$user" > /dev/null
echo "Username and password were created successfully"
