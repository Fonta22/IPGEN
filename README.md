# IPGEN — IP adress generator

## Description
This program generates **fake IP adresses**, that can be stored in a file, or just be printed in the **command line**.
Use the best option for your terminal, **Windows or Unix**.

## Usage
Firstable, navigate to the IPGEN directory with your terminal. If you're on **Unix**, run:
```
source ./ipgen.sh
```
This just allows the command to be run and it's not necessary on **Widows**.
Then, just use the command.
```
ipgen [num] [-s]
```
`[num]`: number of IPs that you want to generate.

`[-s]`: Use this flag only if you want to store the generated IP addresses in a file. The resulting
adresses are stored inside `'logs/ip.log'`.

**Note**: In **Windows** you'll need to add `.\` before the command, so run it like this:
```
.\ipgen [num] [-s]
```

### Resulting log:

After using the command with the `-s` flag, it will return you a **log** like this with the number of **IP**s specified in the other parameter (10 in this case):

![iplog](./_img/iplog.png)

If you want to **clear** the IP log, you can run the following command:
```
ipgen clear
```