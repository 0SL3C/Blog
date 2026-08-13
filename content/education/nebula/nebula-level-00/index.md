---
title: "Nebula: Level 00"
date: 2026-04-13T18:00:00+01:00
draft: false
series: ["Nebula"]
tags: ["exploit.education", "privilege-escalation", "suid"]
categories: ["Hacking"]
summary: "Finding a **SUID** binary owned by `flag00` and abusing it to escalate privileges on exploit.education's Nebula VM."
---

The goal of this level is to find a Set User ID program that will run as the "flag00" account.

[Setuid](https://en.wikipedia.org/wiki/Setuid) is a Unix access rights flag that allow users to run an executable with the file system permissions of the executable's owner.

For example the following executable:

```sh
$ stat /usr/bin/passwd
  File: /usr/bin/passwd
  Size: 63736     	Blocks: 128        IO Block: 4096   regular file
Device: 801h/2049d	Inode: 2237        Links: 1
Access: (4755/-rwsr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
```

will be executed as root (Uid 0), no matter what the current user is. This allows un-privileged user to change their password by editing `/etc/shadow` (root owner) using passwd.

Now going back to the challenge, we can use `find` to search for programs that have SUID by using the flag `-perm -u=s`, where the flag `-perm` checks for the file **permission bits** and `-u=s` defines that check to **SPECIAL BIT (X000)**, so in short the command will bring any file that has a special bit, including SUID.

Now joining everything, and piping errors to `2>/dev/null` for better readability:

```sh
find / -perm -u=s 2>/dev/null
```

OR

```sh
find / -perm 4000 2>/dev/null
```

This is enough to find the file, but we can filter even more by using `grep` and passing the user `flag00` as requested by the challenge.

```sh
find / -perm -u=s 2>/dev/null | grep flag00
```
