Training Project For Sircles

## sorint start course101

1. **Exercise 1**
	Create a folder called `exam` in the home directory and create 3 folders inside it `txt` `mp3` `mp4`
2. **Exercise 2**
	Redirect the first 10 lines of the file `days.txt` which exist in the home directory to the file `/home/sorint/exam/txt/head.txt`
	Redirect the last 7 lines of the file `days.txt` which does exist in the home directory to the file `/home/sorint/exam/txt/tail.txt`
3. **Exercise 3**
	Redirect the value of the `$HOME` and `$PATH` environment variables to the file `/home/sorint/exam/txt/env.txt`
4. **Exercise 4**
	Create the file `/home/sorint/exam/txt/whoami.txt` and edit it using your favourite editor (nano, vim) and put inside it you name and email in this same context. **It is only local at your PC**
```java
name: <XXXX XXXXX>
email: <XXXXX@XXXXX.XXXX>
```
5. **Exercise 5**
	Inside the folder `/home/sorint/random` there are plenty of random files
	- Move all `.mp4` files to `/home/sorint/exam/mp4/` directory *that you have created before*
	- Move all `.mp3` files to `/home/sorint/exam/mp3/` directory *that you have created before*
	- Delete all `.wav` files from the `/home/sorint/random` directory
6. **Exercise 6**
	Check the content of the file `/home/sorint/code.txt` for the code `ansible-api-token=XXXXXXXXXXX` copy the code `XXXXXXXXX` to the file `/home/sorint/exam/txt/token.txt`
7. **Exercise 7**
	Create two groups :
		`devops`
		`testers`
8. **Exercise 8**
	Create the users:
		`developer1`
		`tester1`
	Create a password for the users, the password is **`sorint`**
9. **Exercise 9**
	Append (*add*) the user `developer1` to the group `devops`
	Append (*add*) the user `tester1` to the group `testers`
10. **Exercise 10**
	Create the directory `/partage` 
	Change the ownership of the directory to user `tester1` and the group `sorint` using the `chown` command `tester1:sorint`
	Create symbolic link for the folder `/partage` to the folder `/tmp/shared`
11. **Exercise 11**
	Create the alias `ipa="ip --color a"`
	And the alias must stay persistent after reboot

### sorint grade course101


## sorint start course102

1. **Exercise 1**
	Check all the sleep processes that are running in the background deactivate them all
2. **Exercise 2**
	Enable `sshd.service`
	Disable `chronyd.service` 
	Stop `httpd.service`
1. **Exercise 3**
	there is a failed ssh login attempt used by the user `bernard` and you need to find the **IP address** associated with the failed login and copy it to the file `/home/sorint/exam/txt/ip.txt`
4. **Exercise 4**
	For this exercise you need to generate two ssh keys one normal  and use it to ssh to the second machine we created before, and also to ssh to the remote host without using the password 
	and generate the second one called `sorintKey`
### sorint grade course102


## sorint start course103

1. **Exercise 1**
	There is a need to set the hostname to `alma9.sorint.exam.com`
2. **Exercise 2**
	The second interface with the connection name `sorint` needs to have these info
	Mode : Manual
	IP Address: 172.168.1.200/24
	Gateway: 172.168.1.1
	DNS Server 1 : 172.168.1.1
	DNS Server 2 : 1.1.1.1
1. **Exercise 3**
	There is an important information about the RPM package `sorint-1.3-1.noarch` and there is a code in the summery must be copied to the file `/home/sorint/exam/txt/rpmcode.txt`
4. **Exercise 4**
	We need to install the package `httpd` and then **enable**, **start** it.
5. **Exercise 5**
	Add the services `http` and `https` to the firewall.
6. **Exercise 6**
	Add the `librewolf` Browser Repo to your system using these info:
	It should be `enabled` and `GPG` check is active

```java
name: LibreWolf

baseurl: https://rpm.librewolf.net

gpgkey: https://rpm.librewolf.net/pubkey.gpg#
```
and then check if you can download `librewolf` package

7. **Exercise 7**
	Create the folder `/external` and mount the disk `/dev/sdb` to it
	The folder `/external` should be owned by the user and the group `sorint`
9. **Exercise 8**
	You have a folder called `random-d3` in the home directory
	We have to `find` all the files end with `.txt` extensions and redirect the output to the file `/home/sorint/exam/txt/texts.txt`
	We have to `find` all the files that contains the word `sorint` in their names and redirect the output to the file `/home/sorint/exam/txt/sorint.txt`
10. **Exercise 9**
	We have to allow all the users in the group `sorint` to use the `sudo` privilege without using the password
 
### sorint grade course103
