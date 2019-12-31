# db5
shell  repositor
#!/bin/bash
read -p "请输入您的用户名：" user
useradd "$user" > /dev/null
echo "用户创建成功"
stty -echo
read -p "请输入您的用户名密码：" pass
stty echo
echo "$pass" | passwd --stdin "$user" > /dev/null
echo "用户密码创建成功"
