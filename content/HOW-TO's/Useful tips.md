
check user logs {
	
	/var/log/auth.log
	
}

setup different nameservers {
	server {
		server_name subdomain1.example.com;
			location / {
			proxy_pass       http://hostname1:port1;
			}
	}
	server {
		server_name subdomain2.example.com;
			location / {
			proxy_pass       http://hostname2:port2;
			}
	}
}

- nginx config file:
```sh
	/etc/nginx/nginx.conf
```


{
To port forward to your WSL2 instance from your public IP when connecting on port 3000, you'll need to perform a series of steps involving setting up port forwarding on your Windows machine and configuring your network correctly. Here's a detailed guide:

1. **Identify Your WSL2 IP Address**:
   - Open a WSL2 terminal and run the following command to get your WSL2 IP address:
     ```sh
     ip addr | grep eth0
     ```
   - Look for the `inet` address under `eth0`, which should look something like `172.x.x.x`.

2. **Enable Port Forwarding on Windows**:
   - Open a PowerShell window with administrative privileges (right-click on PowerShell and select "Run as administrator").

3. **Set Up Port Forwarding**:
   - Run the following command to create a port forwarding rule from your Windows host's public IP port 3000 to your WSL2 instance's port 3000:
     ```powershell
     netsh interface portproxy add v4tov4 listenport=3000 listenaddress=0.0.0.0 connectport=3000 connectaddress=<WSL2_IP>
     ```
     Replace `<WSL2_IP>` with the IP address you found in step 1.

4. **Allow Port Through Windows Firewall**:
   - You also need to allow traffic through port 3000 on your Windows firewall. Run the following command in the same PowerShell window:
     ```powershell
     netsh advfirewall firewall add rule name="WSL2 Port 3000" dir=in action=allow protocol=TCP localport=3000
     ```

5. **Verify Port Forwarding**:
   - Ensure your application inside WSL2 is running and listening on port 3000.
   - You can use a tool like `netcat` or simply start your server (e.g., a Node.js server) to listen on port 3000.

6. **Check Connectivity**:
   - From an external machine or using a tool like `curl`, try to connect to your public IP on port 3000 to verify the port forwarding works:
     ```sh
     curl http://${publicIP}$:3000
     ```

### Additional Notes:

- **Public IP Considerations**: Ensure your public IP is static or appropriately managed if it changes dynamically.
- **Router Configuration**: If your machine is behind a router, you may need to configure port forwarding on the router to forward port 3000 traffic to your Windows machine.
- **Security**: Be mindful of security implications when opening ports to the public internet. Ensure your WSL2 service is secured and consider using a firewall or VPN to restrict access.

By following these steps, you should be able to forward traffic from your public IP on port 3000 to your WSL2 instance, allowing you to access your WSL2 service externally.
}
