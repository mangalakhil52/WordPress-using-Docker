# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:57:06 2020

@author: Akhil mangal 
"""
import os
while True:

    print("""
          \n\n\n\t--------------------------------------------------------\n  
          \t\t\t### WELCOME TO DOCKER WORLD ###\n                                            
          \t--------------------------------------------------------            
          \n\n\t\tpress the following keys to perform following actions:\n\t\t  
          press 1: for docker installation                                      
          press 2: for docker yum error                                         
          press 3: for docker-compose installation                              
          press 4: for launch wordpress site with mysql database 
          press 5  for stop the wordpress container            
          press 6: for see docker                                            
          press 7: for see containers running                                                                     
          
          
          
          
          press 0: for exit                                                     
                                                                                
                                                                                 
          ************************************************************************
          """
          
          )
    
    choice  = int(input("Enter your choice ::"))
     
    if choice == 1:
        os.system("yum install docker-ce --nobest")
    elif choice == 2:
        os.system("firewalld-cmd --zone=public --add-masquerade --permanent")
        os.system("firewalld-cmd --zone=public --add-port=80/tcp")
        os.system("firewalld-cmd --zone=public --add-port=443/tcp")
        os.system("firewalld-cmd --reload")
        os.system("systemctl restart docker")
        printf("/n/n/tNOW your docker yum problem is solved Go and check................")
    
    
    elif choice == 3:
        os.system(' curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        os.system(" chmod +x /usr/local/bin/docker-compose")
    
    
    elif choice == 4:
        while True:
            os.system("clear")
            print("\n\nif you don't have wordpress and mysql image then follow these steps:\n\n")
            print("\n\t\tpress 1: for wordpress image ")
            print("\t\tpress 2: for mysql image")
            print("\n\n\tif you already have these images then follow to launch wordress ")
            print("\n\t\tpress 3: for launch wordpress server\n\n\n")
            print("\n\n\tpress 0: Back to main menu")
            choice1 = int(input("Enter your choice : "))
            if choice1 == 1:
                os.system("docker pull wordpress:5.1.1-php7.3-apache")
            elif choice1 == 2:
                os.system("docker pull mysql:5.1")
            elif choice1 == 3:
                os.system("docker-compose up -d")
            elif choice1 == 0:
                exit(1)
            else:
                print("oops wrong input try again.....................")
    
    
    
    
    elif choice == 5:
        os.system("docker-compose down -d")
    
    
    elif choice == 6:
        os.system("docker images ")  
    
    
    elif choice == 7:
        os.system("docker ps")    
    
    
    
    elif choice == 0:
        exit()
    
    
    else:
        print("ohhoo wrong input please try again.................")   
        x= input("PRESS ENTER TO CONTINUE")